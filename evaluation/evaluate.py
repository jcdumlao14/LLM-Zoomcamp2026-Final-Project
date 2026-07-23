import os
import sys
import json
import time
import pandas as pd

# =====================================
# Add Project Root to Python Path
# =====================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)

from app.service import ask

# =====================================
# Load Evaluation Questions
# =====================================

with open(
    "evaluation/test_questions.json",
    "r",
    encoding="utf-8"
) as f:
    questions = json.load(f)

results = []

print("=" * 60)
print("Running MedRAG AI Evaluation")
print("=" * 60)

# =====================================
# Evaluation Loop
# =====================================

for i, item in enumerate(questions, start=1):

    question = item["question"]

    print(f"\n[{i}/{len(questions)}] {question}")

    start = time.time()

    try:

        result = ask(question)

        elapsed = time.time() - start

        answer = result["answer"]

        sources = result["sources"]

        status = "Success"

        print(f"✓ Completed in {elapsed:.2f} sec")

    except Exception as e:

        elapsed = time.time() - start

        answer = f"ERROR: {str(e)}"

        sources = []

        status = "Failed"

        print(f"✗ Failed: {e}")

    results.append(
        {
            "question": question,
            "status": status,
            "answer": answer,
            "response_time_sec": round(elapsed, 2),
            "num_sources": len(sources),
            "source_files": ", ".join(
                doc["filename"] for doc in sources
            ) if sources else "",
            "avg_distance": round(
                sum(doc["distance"] for doc in sources) / len(sources),
                4,
            ) if sources else None,
            "answer_length": len(answer)
        }
    )

    # Small pause to reduce API rate pressure
    time.sleep(2)

print("\nEvaluation completed.")

# =====================================
# Save Results
# =====================================

df = pd.DataFrame(results)

output_file = "evaluation/results.csv"

df.to_csv(output_file, index=False)

print(f"\nResults saved to {output_file}")

# =====================================
# Summary
# =====================================

successful = df[df["status"] == "Success"]
failed = df[df["status"] == "Failed"]

print("\n" + "=" * 60)
print("Evaluation Summary")
print("=" * 60)

print(f"Total Questions : {len(df)}")
print(f"Successful      : {len(successful)}")
print(f"Failed          : {len(failed)}")

if len(successful) > 0:

    print(f"Average Response Time : {successful['response_time_sec'].mean():.2f} sec")
    print(f"Average Sources       : {successful['num_sources'].mean():.2f}")

    if successful["avg_distance"].notna().any():
        print(f"Average Distance      : {successful['avg_distance'].mean():.4f}")

print("\nDetailed Results\n")

print(
    df[
        [
            "question",
            "status",
            "response_time_sec",
            "num_sources",
            "avg_distance"
        ]
    ]
)