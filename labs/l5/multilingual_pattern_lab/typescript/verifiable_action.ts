export type PlanStep = {
  intent: "clarify" | "execute" | "verify";
  tool: string;
  rollbackHint: string;
};

export type PatternResult = {
  steps: PlanStep[];
  stopReason: "ready_for_execution" | "blocked_by_safety_rule";
};

export const SAFETY_RULE = "delete_all";

export function plan(request: string, safetyRules: string[] = [SAFETY_RULE]): PatternResult {
  if (safetyRules.some((rule) => request.includes(rule))) {
    return { steps: [], stopReason: "blocked_by_safety_rule" };
  }
  return {
    steps: [
      { intent: "clarify", tool: "validator", rollbackHint: "remove unclear fields" },
      { intent: "execute", tool: "tool_gateway", rollbackHint: "restore previous state" },
      { intent: "verify", tool: "eval_probe", rollbackHint: "disable path" },
    ],
    stopReason: "ready_for_execution",
  };
}
