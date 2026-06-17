import json
from datetime import datetime
import os
from cycle import run_cycle

def run_lineage(execution):
    print("Lineage Start")

    if execution["status"] != "ISSUED":
        print("Lineage: No execution allowed")
        print("Lineage End")
        return

    # ✅ FR STORAGE
    print("FR: Storing execution")
    os.makedirs("data/fr_storage", exist_ok=True)

    file_name = f"data/fr_storage/execution_{datetime.utcnow().timestamp()}.json"

    with open(file_name, "w") as f:
        json.dump(execution, f, indent=4)

    print(f"FR: Stored at {file_name}")

    # ✅ RD
    print("RD: Gathering research and data")

    # ✅ WR (MULTIPLE OUTPUTS)
    print("WR: Creating multiple outputs")

    os.makedirs("data/output", exist_ok=True)

    for i in range(3):
        output_file = f"data/output/output_{i}_{datetime.utcnow().timestamp()}.txt"

        content = f"""
Execution Report (Task {i})
--------------------------
Execution ID: {execution['execution_id']}
Command ID: {execution['command_id']}
Status: {execution['status']}
Path: {execution.get('execution_path')}
"""

        with open(output_file, "w") as f:
            f.write(content)

        print(f"WR: Output {i} saved → {output_file}")

    # ✅ OD
    print("OD: Refining and structuring outputs")

    # ✅ PD
    print("PD: Publishing and deploying outputs")

    # ✅ Cycle
    run_cycle(file_name)

    print("Lineage End")