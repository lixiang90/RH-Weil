# C069 source-produce metadata builder

2026-11-01; metadata author /root/c069_metadata_builder. This helper launches no
process and imports no controller, observer, source or finite module. It only
reads code/prose/JSON metadata, hashes source files as opaque bytes, and, when
explicitly invoked by ROOT, writes once-only admission metadata. It does not
write STATE, the contract, a runtime Goal or numerical outputs. Its implementation
is not itself ROOT authorization or independent mathematical acceptance.

`plan` is read-only, validates the actual nine frozen code pins, contract,
published closure, six math pins, four opaque input hashes and both review texts,
and emits a compact definition of the paths, schemas and budgets. With an
existing ROOT authorization file it also constructs the entire prepare graph in
memory and outputs its prospective immutable pins. It does not create a dry-run
token, metadata directory or execution namespace.

```
python reviews/2026-11-01/global-joint-execution/build-source-admission.py plan
python reviews/2026-11-01/global-joint-execution/build-source-admission.py plan --root-authorization-file ROOT_AUTH_RELATIVE_PATH
```

Only ROOT may invoke these writing commands after consuming the independent
admission audit. The author of this helper does not invoke either command.

```
python reviews/2026-11-01/global-joint-execution/build-source-admission.py prepare --root-authorize --root-authorization-file ROOT_AUTH_RELATIVE_PATH
python reviews/2026-11-01/global-joint-execution/build-source-admission.py finalize-after-ready --root-authorize --root-live-observation-file ROOT_LIVE_RELATIVE_PATH
```

ROOT's authorization file is immutable and outside `source-produce/`. Required
schema is `RH_WEIL_C069_ROOT_SOURCE_METADATA_AUTHORIZATION_V1`, status
`ROOT_AUTHORIZED_ONE_SOURCE_PRODUCE_METADATA_GRAPH`, runtimeGoalCreatedAt
1793085111, contractId C069 and targetId
`RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1`. Required booleans
`rootRuntimeGoalCheckedActive` and `codePreparationActualFinalVerified` are true;
ROOT must actually make those observations immediately before authorization.
`rootAdmissionNonce` is a new 16..128 character alphanumeric/underscore/hyphen
nonce. `contractPin` and `codeClosurePin` are exact raw-byte pins for the actual
C069 contract and published root-code-closure.json. The required
`rootAdministrativeReservePlanPin` pins ROOT's reserve plan below. Optional
`extraChargedMetadataPins` is a path-to-pin map of other immutable new ROOT
records, including root audits and startup evidence. Do not include mutable STATE
or any report that will subsequently be appended. Each pin has exactly path,
bytes and lowercase full SHA256, and every path is workspace-relative canonical.

The reserve plan has schema
`RH_WEIL_C069_ROOT_ADMINISTRATIVE_RESERVE_PLAN_V1`, status
`ROOT_PREPAID_CURRENT_C069_MUTABLE_ADMINISTRATIVE_OUTPUTS`, the same Goal/C069/
target, `prechargedBytes=1048576`, `nonRefundable=true`, a nonempty
`mutablePathPolicy` map/list, and a nonempty `cumulativeWritePolicy` map/string.
ROOT and its independent consumption auditor establish the exact disjoint path
scope and actual cumulative writes, including mutable STATE/checkpoints and tool
copies outside the five observer destinations. This helper checks the plan's
shape and pin, not the truth of a future write ledger. The full 1MiB reserve
remains paid forever; immutable contract/auth/plan/builder/notes/ARM/READY/gate/
freeze and other child-pinned files are charged additionally, without refund or
discount. A zero prior scientific time and empty prior science/inventory do not
mean zero current C069 metadata charges. Source and aggregate prior bytes are
1MiB; finite prior bytes are zero. Mutable STATE is not pinned.

The seven prepare outputs, all under the fresh builder-owned directory
`reviews/2026-11-01/global-joint-execution/source-produce`, are observer/source
prior accounting, observer/source irrevocable admissions, prepared-context,
observer-arm-root-gate and observer-arm JSON. The context contains the before-ARM
opaque source pins; finalize does not spend the 60s handshake rehashing large
source arrays. The scientific controller rehashes them before source evaluation.
Prepare requires both science and observer run-01 namespaces absent and claims
the metadata directory once. It never creates either execution namespace.
Every raw write uses exclusive create and fsync, with no overwrite/cleanup/retry.
An interrupted partial graph is retained for ROOT disposition.

The DAG is deliberately acyclic: the ARM gate stores only the ARM relative path;
ARM pins its gate. READY, written by the actual observer, pins ARM and the actual
observer claim. The scientific root gate pins READY and stores only the final
freeze relative path; freeze pins that scientific root gate. No record contains
its own SHA or the SHA of a successor. Final source chargedMetadataPins contain
all initial ARM metadata, ARM gate/ARM itself, actual observer claim, immutable
ROOT live observation and optional final ROOT records. The exact source
controller additionally charges READY, contract/admissions/prior, final gate and
freeze with path deduplication. It receives the prepaid 1MiB prior as well.

The live-observation record has schema
`RH_WEIL_C069_OBSERVER_LIVE_ROOT_OBSERVATION_V1`, status
`ROOT_OBSERVED_READY_PID_AND_LIVE_SESSION`, same Goal/C069/target, phase
`source-produce`, positive integer `observerPID` equal to actual READY,
`readyPin` for actual ready.json, `handle_type="exec_command"`, actual nonempty
`handle`, `liveStatus="running"`, `actualToolHandleObservedLive=true`, and
`observedUTC` with UTC offset. ROOT must save the real session and READY/PID in
STATE before invoking finalize. Optional `additionalChargedMetadataPins` holds
immutable final root audit records. The record lives outside both owned runtime
namespaces. The builder validates full READY/claim/ARM binding, requires READY
age <=50 seconds and live observation <=30 seconds, and checks actual kernel
PID liveness twice using a synchronize-only OpenProcess handle. It cannot
independently query the external exec session; ROOT's actual tool observation is
an explicit premise. It does not manufacture a PID or session. Before commit it
requires READY age <=52 seconds and no observer terminal; actual observer funding
checks before child creation/resume remain authoritative. Failed/expired
handoff preserves the same irrevocable attempt; there is no automatic relaunch.

The whole new C069 responsibility remains7200s/64MiB, source+independent
verification3600s/48MiB and finite+independent verification3600s/16MiB. The first
source-produce phase allowance is1500000ms, external child ceiling1380000ms,
internal scientific cutoff1200000ms and ARM wait60000ms. These are limits, not
measured charges. Future phases receive only actual remaining resources and are
never dispatched by this helper. The exact external map is stdout16384,
stderr16384, child8192, terminal131072 and root-observed131072 bytes in the
source-produce observer directory: total303104 <=524288. All new helper stdout,
tool copies and metadata are charged through ROOT's explicit plan or immutable
child metadata map. Existing published source/code/prose are read-only inputs.

The source review vector is ordered controller/producer/verifier, with exact
full SHA256 values
0188ebfe2a0565bcfa53687a82b4dad068b57aae4413d3ff2aed18f8e7a7c9d9,
89bb4eb23264b6f7d1bd56459e2d7825b94ec5a02e5ff7c36e6cc0bfa1237975,
2b1c1de335e2412c2f6e1cec7a219f3bd496561df6f4d134a5c87ea42a7603db.
Protocol is fe70954d6716290bc5b8421fa236d775aefb99e3f3819d777ec72e9ca89c7161;
observer is88d54d68d5119aff6eacc6581a3de56d53f9121ffacc3a6c17e7f87df8c4637d.
ROOT's published root-consumed.md is the math/package candidate, owner /root;
observer-final-protocol-review.md is the protocol candidate, distinct owner
/root/global_independent_verifier. Both raw texts must contain all these full
SHA values and the declared owner. ARM reviews use separate observerSHA256/
childSHA256 fields. The builder checks all nine code pins against both hardcoded
actual-final byte/SHA identities and the published ordered closure vector.

Source emission, packet/hash checks and these metadata gates do not establish
independent arithmetic230, finite216, the selected target sign, the whole
fixed9/8 claim, RH, or Goal completion. Any admitted terminal failure consumes
the same C069 responsibility. ROOT retains the full pre-ARM/post-exit UTC,
process-coverage/multiplicity and cumulative-output consumption duties.
