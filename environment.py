from utils.healing_agent import analyze_and_heal_failure

def after_step(context, step):
    if step.status == "failed":
        error_msg = str(step.exception)
        context_data = {
            "feature": context.feature.name,
            "scenario": context.scenario.name,
            "step": step.name,
        }
        healing_suggestion = analyze_and_heal_failure(error_msg, context_data)
        print("\n💡 Healing Suggestion by LangChain:")
        print(healing_suggestion)
