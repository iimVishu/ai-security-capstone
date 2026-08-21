# Risk Assessment

## Current status

Risk ratings are pending because the actual MCP capability inventory is unavailable. No arbitrary rating is assigned.

## Rating basis

- **High:** capability can execute code, alter/delete data, access secrets, or cross a trust boundary with meaningful impact.
- **Medium:** capability can modify non-critical lab data, access sensitive context, or enable a meaningful multi-step chain.
- **Low:** read-only, tightly scoped, non-sensitive capability with no evident side effect.

## Required record

For each discovered capability, document: Capability, Type, Risk, Reason, Potential abuse scenario, and Recommended mitigation. Mitigations should include least privilege, explicit user confirmation for side effects, input validation, output sanitization, resource provenance checks, and audit logging where relevant.