# 固定9/8：六模块 source-only worker 实现与待执行边界

2026-10-29。仅实现/prepare，不执行 moments、matrices 或 tails；不改 STATE、cadence、Git、Goal。新 worker 是 `scripts/weil_9_8_source_pilot.py`。所有第三方原件、修改副本、manifest和未来数值 packets 都在被忽略的 `literature/local/2026-10-29-weil-9-8/` 下；本记录只公开来源与实现范围。

## 1. 当前实际产物与固定身份

`python -I -S -B scripts/weil_9_8_source_pilot.py prepare` 已完成一次 prepare-only：六份原件 SHA256、逐处 replacement 的准确 hit count、去历史 CLI、纯模块 AST、全部副本编译通过。原件未修改。没有数值证书、stage receipt 或运行中的科学进程；`pilot/run-01/certificates/` 和 `receipts/` 在本次结构核查时均为空。

| 绑定 | SHA256 |
|---|---|
| 新 worker | `7589b854cbcd2f1c2fcdf0ecce60b614af7e1d73992b6f64719e1624a0ad0961` |
| ignored `pilot/source-manifest.json` | `15ae30f087481a40d9c9d6bf3ff517ea1e50aba04b3899fcdd049c55364511e4` |
| canonical configuration | `8e4e59c11469cf35e5ad2e85a433660e6720ebd322d7ffd5c87d805cf2c0d364` |

固定源 commit 为 `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`。worker硬绑定 root 恢复收据中的六原件 SHA，而非下载时的可变 branch。prepare 会先在内存构造并编译全部副本，所有预检完成后才写出；已有 SOURCE/manifest 时拒绝重复prepare。数值各 stage 同样拒绝任何既有 packet/receipt/access/failure 输出，保留一次固定尝试的证据。

| 模块 | 原SHA256 | 新副本SHA256 | bytes | patch events |
|---|---|---|---:|---:|
| 01-check.py | `4ed7661f1f869ed6d37d7bc52f1a0889a8d305a790663dc0ae43d76f2ea0e356` | `8d2e73a49846272f7fadeb037e1efa44daeb84318354f5c53c502c44d28bb288` | 13581 | 8 |
| 02-produce.py | `0b338cf043e8bcf2c22e3f9cd26914d3b39a00b03f13070b0de02b7a9210556a` | `792ee1c93291459ca903b6f4f5e3c4f051f2463a1a020eac756b13fa6b913337` | 6946 | 5 |
| 07-check.py | `bee8f860c1919059e8888be3e8941bfd6dd592f467165d53ef8ec04fcd532635` | `85fcaaefd2d752a8401b9f7686c1c8779282c2cc21504129aabda7d1e37a83de` | 19517 | 31 |
| 08-produce.py | `7b980b6dd8ff7a8dd0163cef970f3bf8ac9dff8bddb6b2762d56669e2723680d` | `ae0f487544c203905faecbb78b30f94fb16fe4f2f63c6b9846ca13ea673ba2b7` | 9863 | 20 |
| 11-checker_quotient.py | `c951ce0d4075c3b93739901f6aa938421841ab183b816172b2685ffac5bbce8a` | `ea6f8ed0e2780aa2835bb75f1a7e08fd807220ac4eb1b14f8c6aa0834e331af3` | 7899 | 6 |
| 12-raw_column_producer.py | `6342dca29469c61034aa39c5a648285691244ef6863a4fe9f2de3a0af07f516e` | `a8a67b4e08d540f51e152fe05bd19d77ae69fc618e4d6c08cb24c730b3afbb9c` | 5460 | 3 |

## 2. 可执行范围与参数

只提供 `prepare`, `isolation-test`, `moments`, `matrices`, `tails` 五个入口。没有 core、trial inverse、congruence、Gram、全Q/PSD/RH入口。运行时强制 `-I -S -B` 与 assertions；不得 import 原 run.py/stage.py/scalar.py/reproduce.py。六副本去掉历史 main；只从纯函数入口生成和独立检查。

所有科学 stages 必须显式给 `--manifest-sha` 与 `--worker-sha`，并绑定同一个 configuration digest。所有 source pins/输入 pins 在开始与完成均重核；模块每次 load 再核 bytes/AST/SHA。运行时 exact read/write allowlist、标准库范围、无 site-packages、未知 descriptor 与网络/process/ctypes deny；audit-access JSON 保所有open和违规。isolation-test只有拒绝外部read/socket/subprocess三项，不生成数值。该证据是Python audit hook，非OS syscall sandbox。

固定半窗9/8、Ω256、N448、1024 moments，prime powers2/3/4/5/7/8/9。moments producer6144、checker6400、output1152、radius1098；matrices3072/3328、center2048、output256；rawtail2048/output640、Machin160。无精度、L、weight或degree搜索。

01/02 保留 true-digamma-moment 的 Binet包含逻辑（02在 `m.sym` 支付一次），只更改1152输出与一致性、containment、radius标签。moment packet 使用全新 schema，matrix入口必须同时核 parameters 的类型/全部键值、1152精度、Binet-once标记、同 worker/manifest/config digest、complete checker receipt 和 packet SHA。原stage只取rows的缺口被关闭；不借旧1024-width==3捷径。

07/08 增加±9，Λ(9)=log3，shift log9=2log3。producer按两倍log3，checker独立直接log9；各有 log10>9/4 的有向门，足以排全部n≥10。15中心、225 ordered pairs、全部max-three/min-three overlap、one-sided B endpoint保留。权总质量改<11并实际 directed检查；raw padding保持2^-2021但其来源Lipschitz数学费由root单独闭合。L采用18/16编码：metric18/q、L²81/64、kernel576²、moment midpoint分母1153；不全局替换17。原fixture宽改5/4，对错误缺约束7/4执行拒绝。全部151200 intervals、每矩阵50400、有序扩展100576、updates99681及448 weighted rows均由原独立算术结构再验。

矩阵packet经07 `verify_packet` 完整新schema/identity/errors/convention验证，复用全部9个mutation controls，包含同宽平移必须落到actual containment拒绝；不是原stage的仅两项弱控制。tail用12 recurrence与11 independent factorial quotient全896 coordinates/448 parity zeros；另加缺坐标、错误mid、非零parity与同宽平移四个控制。最后一项须具体触发 `INDEPENDENT_ENCLOSURE_NOT_CONTAINED`。这些controls尚未执行，不能先报通过。

## 3. 状态与停止

成功 stage 的状态统一为 `SOURCE_ONLY_NOT_FULL_Q`，显式 `analyticErrorFeesPaid:false`, `fullQCertified:false`, `coreStageAdmitted:false`。tail原replay中normalized512/ranktwo510标签在副本改为null，不冒领全operator解析误差；当前仅认证raw finite columns。root另付 kernel576、Binet一次、全sinc/pole/projection/Schur/complement等实际费用。source成功也不能代新逆order、目标正号或all-Dlog全Q结论。

任何算术/width/containment/control失败写 NONPASS、traceback和access，保已有产物，不删除重跑或自动提升精度。preflight SHA/config/collision失败在进入算术前拒绝，终端错误由root launcher保存。未消费旧mu29/32、旧target bit/exponents或旧PASS。需要root先消费固定新mu及相关完整预算，再决定是否运行一次source-only尝试；本子任务没有自行授予或执行该动作。

准备后结构核查实际验证了六副本参数、SHA、patch统计、空certificates/receipts，并用 `git check-ignore` 确认manifest和副本被忽略。没有数值结果，无数学计轮；核心算术primitive/principal/mixed和growing-core瓶颈未变化。
