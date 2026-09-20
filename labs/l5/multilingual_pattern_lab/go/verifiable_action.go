package main

import "strings"

const (
	safetyRule       = "delete_all"
	readyReason      = "ready_for_execution"
	blockedReason    = "blocked_by_safety_rule"
)

type PlanStep struct {
	Intent        string
	Tool          string
	RollbackHint  string
}

type PatternResult struct {
	Steps      []PlanStep
	StopReason string
}

func readyPlan() PatternResult {
	return PatternResult{
		Steps: []PlanStep{
			{"clarify", "validator", "remove unclear fields"},
			{"execute", "tool_gateway", "restore previous state"},
			{"verify", "eval_probe", "disable path"},
		},
		StopReason: readyReason,
	}
}

func plan(request string, safetyRules []string) PatternResult {
	for _, rule := range safetyRules {
		if strings.Contains(request, rule) {
			return PatternResult{StopReason: blockedReason}
		}
	}
	return readyPlan()
}

func main() {
	rules := []string{safetyRule}
	if plan("update profile", rules).StopReason != readyReason {
		panic("expected ready plan")
	}
	if len(plan("delete_all", rules).Steps) != 0 {
		panic("expected blocked plan")
	}
}
