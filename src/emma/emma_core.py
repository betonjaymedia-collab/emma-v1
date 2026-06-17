from emma.fr_consultation import consult_fr
from lineage import run_lineage

def run_emma(input_data):
    print("Emma Start")

    # Directive
    directive = input_data
    print("Directive:", directive)

    # Mode
    mode = "Architect"
    print("Mode:", mode)

    # FR Consultation
    fr_result = consult_fr(directive, mode)

    # Command
    command = {
        "command_id": "CMD-001",
        "intent": directive.get("intent"),
        "mode": mode,
        "status": "AUTHORIZED",
        "risk_level": "low",   # change to "high" to test blocking
        "confidence": fr_result.get("confidence"),
        "execution_path": "Lineage"
    }

    print("Command:", command)

    # Autonomy Check
    if command["risk_level"] == "low":
        autonomy_status = "CLEARED"
    else:
        autonomy_status = "BLOCKED"

    print("Autonomy:", autonomy_status)

    # Execution
    if autonomy_status == "CLEARED":
        execution = {
            "execution_id": "EXEC-001",
            "command_id": command["command_id"],
            "status": "ISSUED",
            "execution_path": command["execution_path"]
        }
    else:
        execution = {
            "execution_id": None,
            "command_id": command["command_id"],
            "status": "BLOCKED"
        }

    print("Execution:", execution)

    # ✅ HANDOFF TO LINEAGE
    run_lineage(execution)

    print("Emma End")