package main

import "testing"

func TestVerifiableActionBlocksBeforeExecution(t *testing.T) {
	if plan("update profile", []string{safetyRule}).StopReason != readyReason {
		t.Fatalf("expected ready plan")
	}
	if len(plan("delete_all", []string{safetyRule}).Steps) != 0 {
		t.Fatalf("expected blocked plan")
	}
}
