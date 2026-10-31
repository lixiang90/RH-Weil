# Conditional SOURCE-VERIFY interface notes

2026-11-01; metadata/interface readout by /root/c069_metadata_builder. These
notes were obtained by reading the frozen code and ROOT consumption plan. They
contain no actual producer result, packet values, run times, remaining grant,
phase token, authorization or executable. They do not authorize another phase.
ROOT may consider this interface only after the original source-produce session
and all science have actually closed, the producer and observer have succeeded,
and ROOT has consumed complete source/time/output evidence within C069 caps.
The new prose emission belongs to the existing524288-byte nonjournal preparation
partition within the prepaid1MiB administrative reserve, without a new grant.

The controlling exact implementations remain source-stage-controller.py36959,
SHA2560188ebfe2a0565bcfa53687a82b4dad068b57aae4413d3ff2aed18f8e7a7c9d9,
and observe-global-once.py44215,
SHA25688d54d68d5119aff6eacc6581a3de56d53f9121ffacc3a6c17e7f87df8c4637d.
The independent scientific reference is verify-source-model.py26778,
SHA2562b1c1de335e2412c2f6e1cec7a219f3bd496561df6f4d134a5c87ea42a7603db.
No implementation, first-phase frozen graph or source data was changed here.

Let S denote
`literature/local/2026-11-01-directional-remainder-whole/run-01`
and O denote
`literature/local/2026-11-01-directional-remainder-whole-observer/run-01`.
Actual paths below mean these exact strings with the indicated suffix.

## Phase identities and the one original whole owner

The SAME runtimeGoalCreatedAt1793085111, contractId C069, targetId
`RH_WEIL_FIXED_9_8_EXACT_YSTAR_GLOBAL_SCHUR_V1`, science outer S and original
S/run-lock.json remain in force. No new run-01, responsibility or budget begins.
The original outer's `rootAdmissionNonce` is the first source-produce nonce N0.
Read N0 from that actual immutable run-lock.json and first consumed graph; never
invent it or replace the lock. The verify freeze/gate retain
`rootAdmissionNonce=N0` because controller phase_claim verifies equality to the
existing whole lock. The producer PID inside that lock is historical ownership,
not the new verifier's PID or parent PID.

The new source-verify ARM has a distinct fresh phase `armIdentity=N1`.
The observer's actual new READY has `freezeIdentity=launchNonce=N1`; the verify
source freeze/gate have `freezeIdentity=N1`. The new scientific admission token
has phase `verify` and freezeIdentity N1. The observer admission token has phase
`source-verify` and armIdentity N1. Thus the verify freeze simultaneously carries
the old whole `rootAdmissionNonce=N0` and the new phase `freezeIdentity=N1`.
Setting rootAdmissionNonce to N1 would fail OUTER_OWNER_BINDING; carrying the old
READY or old phase identity as the new launch would not bind the new observer.

The observer uses phase `source-verify`; the child controller uses phase
`verify`. Both use the same exact source-stage-controller.py. The scientific
reference is loaded only by that authorized verifier phase, not by this note or
an admission helper. Controller/producer/verifier review-vector order remains
controller0188, producer89bb, verifier2b1, including in verify gates. Parameters,
four source pins, six mandatory math pins, protocol and two distinct-owner final
reviews remain the exact frozen values; no precision/degree/representation edit.

## Exact new observer paths and immutable handoff graph

The existing O/source-produce evidence is retained and frozen. The new exclusive
observer directory is O/source-verify and must not already exist. The exact
five new output destinations are O/source-verify/stdout.txt, stderr.txt,
child.json, terminal.json and root-observed.json. Their individual maxima must
be explicitly frozen and paid from actual remaining SOURCE/aggregate bytes;
they are a new phase's reservations, not reuse of old prepaid paths. The frozen
observer requires individual maxima <=131072, child>=4096, terminal>=65536,
five unique exact paths and total<=524288. No maximal allowance is promised here.

The observer ARM's `finalFreezeRelativePath` must be exactly
O/source-verify/final-freeze.json and `finalRootGateRelativePath` exactly
O/source-verify/final-root-gate.json. Both must be absent at ARM admission and
are written only after the actual new READY and live exec session are observed.
The child source gate's `freezeRelativePath` is exactly that same new final
freeze path. Source freeze's `rootGatePin` pins exactly that final source gate.
Do not use the first source-produce final paths or an absolute source freeze path.

Observer ARM schema is RH_WEIL_GLOBAL_OBSERVER_ARM_V1, authorization
ROOT_EXPLICIT_C069_OBSERVER_ARM_ONLY. Its root gate schema is
RH_WEIL_GLOBAL_OBSERVER_ARM_ROOT_GATE_V1, status
ROOT_EXPLICIT_OBSERVER_ARM_APPROVED. The gate stores the new ARM relative path
as a string; ARM pins that gate. Both exactly repeat phase, runtimeGoalCreatedAt,
contractId, targetId, armIdentity, observerCodePin, childCodePin, contractPin,
rootAdmissionPin, priorAccountingPin, reviewPins, chargedMetadataPins, phaseLimits,
armWaitMaxMs, externalOutputPaths, finalFreezeRelativePath and
finalRootGateRelativePath. The root gate also requires an actual fresh
sameRuntimeGoalLiveAndActiveChecked observation. Contract pin remains the SAME
immutable actual C069 contract used by the first responsibility.

Observer admission schema remains
RH_WEIL_C069_IRREVOCABLE_OBSERVER_ARM_ADMISSION_V1, status
ADMITTED_BEFORE_ARM_NO_RETRY, now phase source-verify, identity N1 and same scope.
ARM review entries use role, distinct owner, pin, observerSHA256 and
childSHA256. They are not the source gate's approvedCodeSHA256 vector schema.
The new actual READY is O/source-verify/ready.json, schema
RH_WEIL_SOURCE_EXTERNAL_OBSERVER_LAUNCH_V1, phase verify, observerPhase
source-verify; it binds the new live observer PID, claim, ARM/gate/prior/admission,
N1, actual observer/controller pins, limits and five output destinations.

The scientific freeze schema is RH_WEIL_GLOBAL_SOURCE_PHASE_FREEZE_V1,
authorization ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION. Its root gate schema is
RH_WEIL_GLOBAL_SOURCE_PHASE_ROOT_GATE_V1, status
ROOT_EXPLICIT_C069_SOURCE_PHASE_EXECUTION_APPROVED. The freeze/gate exactly repeat
phase=verify, runtimeGoalCreatedAt, contractId, targetId, outerRelativePath=S,
parameters, freezeIdentity=N1 and the following fields:

- contractPin, controllerPin, producerPin, verifierPin, protocolPin;
- sourcePins, mathPins, reviewPins;
- launchPin for the ACTUAL new READY, admissionPin for the new source token,
  priorAccountingPin for the new ROOT source accounting;
- chargedMetadataPins, externalOutputPaths, phaseLimits;
- producerResultPin, producerTerminalPin, outerClaimPin, rootAdmissionNonce=N0.

Source admission schema remains RH_WEIL_C069_IRREVOCABLE_PHASE_ADMISSION_V1,
status ADMITTED_BEFORE_LAUNCH_NO_RETRY, phase verify, freezeIdentity N1 and same
Goal/C069/target. Unlike produce, the last three result/terminal/outer pins are
all nonnull: producerResultPin is S/stage-01-source/produce/result.json,
producerTerminalPin is S/stage-01-source/produce/terminal.json and outerClaimPin
is S/run-lock.json. All refer to the already accepted actual first phase.

The new source gate stores only the new final-freeze path; new final freeze
pins its gate. New READY pins ARM/claim. No record hashes itself or a successor.
ROOT records the actual new session/PID/READY in STATE before the final gate.
The existing first-phase builder/handoff helper implement produce-specific
schemas and constants: these notes do not make either usable for verify.

## Two distinct prior-accounting schemas

Prepare new immutable next-phase prior files AFTER consuming/sealing the actual
producer ROOT receipt. Do not modify source-produce/root-observed.json or pin
that receipt to itself. Its actual sealed raw pin can be an input to the new
priors, whose own fees are new paid metadata. Prior time, charged byte uppers,
paid reserves and all retained immutable path bindings carry forward monotonically.
The prepaid1MiB administrative reserve is already included in the first source
terminal charge; do not add it again, refund it or reset it to current file sizes.

The source-controller prior schema is
RH_WEIL_ROOT_OBSERVED_GLOBAL_ACCOUNTING_V1, status
ROOT_VERIFIED_NO_RETRY_ACCOUNTING, same Goal/target and outerRelativePath=S.
Its required fields are sourceObservedUpperMs, aggregateObservedUpperMs,
sourceChargedUpperBytes, aggregateChargedUpperBytes, phaseLifetimes,
outerPreviouslyCreated=true, chargedPathBindings, producerTerminalPin and
outerClaimPin. The last two equal the verify freeze's same fields.

For source verify, phaseLifetimes must contain exactly ONE entry whose phase is
`source-produce`, fullObservedUpperMs is positive, exitCode is0,
`enclosedKernelAddedAgain=false`, and terminalPin equals producerTerminalPin.
The source observed upper dominates that complete root-measured phase charge,
any separately paid SOURCE closure time and the producer terminal's
internalElapsedCeilingMs. Aggregate time is at least SOURCE time; no finite
science has yet occurred. Byte uppers dominate the actual producer terminal's
sourceChargeUpperIncludingTerminalReserve and aggregateChargeUpperIncludingTerminalReserve,
plus any costs not already covered by those paid reservations. Retain every
larger actually paid upper. A producer internal timer alone is insufficient.

The observer prior is a DIFFERENT schema:
RH_WEIL_GLOBAL_OBSERVER_PRIOR_ACCOUNTING_V1, status
ROOT_VERIFIED_ALL_PRIOR_SCIENTIFIC_PROCESSES_TERMINAL, same Goal/C069/target,
noLiveScientificProcesses=true from actual ROOT closure. It uses
sourceConsumedUpperMs, finiteConsumedUpperMs, sourceChargedUpperBytes,
finiteChargedUpperBytes, phaseLifetimes and baselinePins. For source-verify its
phaseLifetimes also contains exactly source-produce, positive fullObservedUpperMs,
exitCode0, but the required no-double-count field is
`enclosedChildAddedAgain=false` (not enclosedKernelAddedAgain). Both spellings can
be retained in a common evidence row, but each schema must have its own required
field. Finite prior time/bytes stay0; SOURCE paid time/bytes carry actual first
phase upper and all other paid SOURCE closure/admin costs. The new child source
prior cannot discount either SOURCE or aggregate costs represented by this ARM
prior: the observer explicitly compares all four child source upper fields.

The two prior records need not have identical field names or byte serialization.
They must describe one consistent actual paid history, with usable complete
process coverage, no live science, and no contradiction between ROOT receipt,
child terminal, observer terminal, actual UTC interval and cumulative ledger.
Every additional scientific process must have its complete actual lifetime
paid; a root-observed phase containing the controller is charged once without
adding the enclosed controller again. Unknown multiplicity/cost blocks admission.

## Path inventory, old paid bytes and new metadata

The source prior's chargedPathBindings is a canonical path-to-raw-pin map, not a
sum of current file sizes. It must include EVERY preexisting retained file under
S, including run-lock, the one canonical packet and all actual produce claim/
progress/result/terminal files. At verifier startup the controller enumerates
all existing S files, subtracts only its own newly created verify claim, and
requires exact equality to the S-subset of chargedPathBindings. Missing or
invented historical files fail; a leftover unaccepted .part is not repaired.
The new S/stage-01-source/verify directory must not preexist; it is exclusively
created by the controller. No extra source inventory/prose should be written
inside S. All previous bindings are rehashed before source recomputation.

Also retain bindings for already paid immutable metadata and old observer
artifacts where their paid authority is established: first admissions/priors/
ARM gates/ARM, old claim/READY, final gates/freezes, root-live, sealed ROOT
receipt, and other actual paid immutable files. Do not pin mutable STATE or a
report still being edited. Previously paid paths in new source metadata must
match their carried pins exactly to avoid both mutation and unnecessary new
static charging. New immutable next-phase metadata is paid separately. The
source controller excludes already bound immutable paths from new_static, but
never refunds prior cumulative rewrites, retired outputs or full prepaid maxima.

The observer prior baselinePins must cover the actual already paid retained
science AND old observer files, plus paid immutable metadata as appropriate.
The observer guard scans BOTH complete S and O trees: any path omitted from
baseline is treated as a new retained file in addition to the carried byte
upper. In particular omitting the existing large packet can cause a false
double charge/cap refusal. Every baseline pin is checked; the observer allows
up to64MiB per baseline file. This is not permission to copy the packet, nor a
fee reset. New phase destinations/READY/claim/gates are not old baseline files.

All new ARM chargedMetadataPins plus the new ARM gate, new admission/prior,
contract and new ARM itself must enter the child's final chargedMetadataPins,
along with the new actual observer claim. The observer checks every such
binding before creating/resuming the child. New READY is the source launchPin;
the source controller automatically adds launch, contract, admission, source
prior, source root gate and source freeze to its static charge map with path
deduplication. Keep the new five output destinations disjoint from all static
and prior-bound paths. Their full frozen maxima and the source terminal reserve
are paid, even if retained terminal/stdout sizes are much smaller.

## Actual remaining funding and scientific result boundary

No initial1500000/1380000/1200000ms limits are automatically renewed. New
phaseAllowanceMs is at most min(3600000-sourceConsumedUpperMs,
7200000-sourceConsumedUpperMs-finiteConsumedUpperMs). Internal cutoff is positive,
at most externalObserverChildTimeoutMs-10000, and external child ceiling plus
20000ms is at most that phase allowance. ARM wait is positive, <=60000ms and
less than phase allowance-30000ms. All interpreter/ARM/hash/setup/kill/finalization
time remains part of the complete SOURCE/aggregate consumption. The observer
again requires ACTUAL remaining child time >=internal+10000ms before creation
and before resume. Nominal inequalities do not guarantee this handoff succeeds.

SOURCE bytes remain at most50331648, aggregate at most67108864; the future
finite16MiB budget is neither transferred nor spent here. New static metadata,
all actual verifier cumulative writes/replacements, full five output reserves
and262144-byte terminal reserve must fit on top of actual carried paid uppers.
Closed proof of remaining resources is required before a new irrevocable token;
a quiet observer, time-limit estimate or retained inventory is insufficient.

Controller additionally requires the accepted producer result status
MODEL_FIVE_BLOCKS_CENTER_CERTIFIED_PENDING_ROOT, target match, rows401856 and
inputPins exactly equal to its four frozen DATA_PINS hashes. Producer terminal
must have status SOURCE_PRODUCER_EMITTED_REQUIRES_INDEPENDENT_CHECK, phase
produce and resultPin matching the accepted producer result. Its packet object
has relativePath S/stage-01-source/joint-centers.jsonl, rows401856 and rawBits256;
actual packet bytes/SHA are taken from that object and checked before and after
independent verification. The one shared packet is read in place, never copied.

Independent success must have status
FIVE_MODEL_BLOCKS_FINAL_CENTER_NATIVE_ARITHMETIC230_VERIFIED,
matching packetSHA256/packetRows401856, bothHermitianTrianglesCharged=true and
exactInfiniteCXOffdiagonalTailIncluded=true. The controller adds packetPin,
producerResultPin and its own/reference/freeze identities, then emits terminal
SOURCE_INDEPENDENT_CHECK_EMITTED_REQUIRES_ROOT_ACCEPTANCE. ROOT must still consume
the actual closed verifier/observer session, original endpoint/native-norm
scientific result and complete time/output ledger before source230 acceptance.
Hash/shape/field success alone is not independent numerical recomputation.

Even accepted source verification leaves C069 unsettled and grants no finite
phase, whole sign, fixed9/8 theorem, growing-window/Ξ consequence or Goal
completion. A failure uses the same irrevocable C069 responsibility, with all
partial artifacts and costs retained and no retry. Later finite stages need
their own ROOT gates on actual remaining resources; these notes create none.
