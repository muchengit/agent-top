const SAFETY_RULE: &str = "delete_all";
const READY_REASON: &str = "ready_for_execution";
const BLOCKED_REASON: &str = "blocked_by_safety_rule";

type PlanStep = (&'static str, &'static str, &'static str);
type PatternResult = (Vec<PlanStep>, &'static str);

fn ready_plan() -> PatternResult {
    (
        vec![
            ("clarify", "validator", "remove unclear fields"),
            ("execute", "tool_gateway", "restore previous state"),
            ("verify", "eval_probe", "disable path"),
        ],
        READY_REASON,
    )
}

fn plan(request: &str, safety_rules: &[&str]) -> PatternResult {
    if safety_rules.iter().any(|rule| request.contains(rule)) {
        (Vec::new(), BLOCKED_REASON)
    } else {
        ready_plan()
    }
}

fn main() {
    let rules = [SAFETY_RULE];
    assert_eq!(plan("update profile", &rules).1, READY_REASON);
    assert!(plan("delete_all", &rules).0.is_empty());
    println!("rust verifiable action ok");
}
