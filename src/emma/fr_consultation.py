import os
import json

def consult_fr(directive, mode):
    print("FR Consultation Start")

    storage_path = "data/fr_storage"

    # Default knowledge
    result = {
        "knowledge": "basic system knowledge",
        "confidence": "medium",
        "reason": "no prior data available",
        "recommended_use": "standard execution"
    }

    # Check if storage exists
    if os.path.exists(storage_path):
        files = os.listdir(storage_path)

        # Only proceed if files exist
        if len(files) > 0:
            files.sort()
            latest_file = files[-1]
            file_path = os.path.join(storage_path, latest_file)

            with open(file_path, "r") as f:
                data = json.load(f)

            print("FR: Retrieved previous execution →", latest_file)

            # Convert execution -> knowledge
            if data.get("status") == "ISSUED":
                result = {
                    "knowledge": "previous execution succeeded",
                    "confidence": "high",
                    "reason": "last execution successful",
                    "recommended_use": "reuse approach"
                }
            else:
                result = {
                    "knowledge": "previous execution failed",
                    "confidence": "low",
                    "reason": "last execution failed",
                    "recommended_use": "change approach"
                }

    print("FR Result:", result)
    print("FR Consultation End")

    return result
