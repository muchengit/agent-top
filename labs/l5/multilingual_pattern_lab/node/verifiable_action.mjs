export const SAFETY_RULE = "delete_all";
export const READY_REASON = "ready_for_execution";
export const BLOCKED_REASON = "blocked_by_safety_rule";

const readyPlan = [
  { intent: "clarify", tool: "validator", rollbackHint: "remove unclear fields" },
  { intent: "execute", tool: "tool_gateway", rollbackHint: "restore previous state" },
  { intent: "verify", tool: "eval_probe", rollbackHint: "disable path" },
];

export function plan(request, safetyRules = [SAFETY_RULE]) {
  if (safetyRules.some((rule) => request.includes(rule))) {
    return { steps: [], stopReason: BLOCKED_REASON };
  }
  return { steps: readyPlan, stopReason: READY_REASON };
}

if (process.argv[1] && import.meta.url === `file://${process.argv[1]}`) {
  console.log(JSON.stringify(plan("update profile")));
  console.log(JSON.stringify(plan("delete_all")));
}
