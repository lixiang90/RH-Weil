# 第505轮联合帧／pair证书与两cutoff覆盖独立审查

2026-10-11，checkpoint_audit，不同作者。限定数学PASS；不运行Lean、Nano或网站检查，不操作Git。
新比例的有限矩阵与连续消费已完整独核；无零部分只准入相对既有引用输入R的覆盖修复，未准入新的mixed upper、count saving或strip。

## 1. 固定身份与实际阅读范围

所有SHA为canonical UTF-8 LF SHA256。全文读取短论文、182行研究checker、163行public checker、两cutoff报告与149行portable checker。
445358字节JSON完整解析并处理每个frame/pair/branch/row/dual，未用保存的PASS字段代替计算。

| 输入 | 行数／LF字节 | SHA256 |
|---|---:|---|
| papers/joint-frame-pair-simple-critical-paper.tex | 293／12286 | 703efcb80e3ff5a37c5bf7b1c4942a986c9bc5c248698b81f23c9f93350d858f |
| scripts/am_joint_frame_pair_certificate.py | 163／11951 | 717570346300346adcc0658761cd979c4756a1666d5591383a642cb8e9221676 |
| output/am-joint-frame-pair-certificate.json | 22350／445358 | cd031c3b3e7daa85f47a52ac4fd3c2d6d8512105c809061b39dfd8fa968b77d7 |
| tmp/.../proportion/certificate505.py | 182／14749 | 8d8ff13c4fb99197f695a348358614ba4e2f0b4fcdcba64046d5b9276ca954a6 |
| tmp/.../proportion/joint-frame-pair-c805448.json | 22350／445358 | e2ad74fe35163d0373694aa4e14e8f05318d6d5471b42275da70ce60ac040073 |
| tmp/.../proportion/joint-frame-pair-c805448-check.json | 49／2000 | 8802dbff5b053eeaf431a7b0b78aeda89f988d771b4191a98f9c1d9f4ca7a46d |
| reviews/2026-10-11/two-cutoff-joint-witness-coverage.md | 378／17730 | a886654b5fdcd13a488f3b32406ef999ef459f427ed56b30d73848ebc7a68e12 |
| scripts/hybrid_two_cutoff_coverage_budget.py | 149／7663 | c9803410aa196f25f2db5a867dd5e56b832ef35627ba76df38f77f6cb7cc1ba4 |

tmp/...表示tmp/research-round505-20261011。public JSON与上述scratch JSON的全部数学payload逐字段完全相同，唯一差别是checker自身SHA。
所有固定dependency pins重新匹配。原PTL源raw SHA为012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f。
原Hecke TeX canonical SHA为42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。

## 2. 独立精确重建的实际收据

只用Python标准库Fraction，在内存执行独立重建，未import任何作者checker。
重用我既有独立审查文件的公式前缀（f3804b0a44a09d46a5116cbbe0ec9d08837fa746940d50eb40b73bd054949c05），自行新写反射、Floyd、joint矩阵、branch与dual计算。
该前缀不含保存结果的写入段。执行命令真实exit0；计时8.0秒是本次算术阶段，无性能或全kernel含义。

```json
{
  "independent_fraction_PASS": true,
  "author_modules_imported": false,
  "all_source_points_checked": 2196,
  "catalog": 425,
  "original_frames": 241,
  "unsplit": 39,
  "split_branches": 4,
  "reflected": 241,
  "candidate_pairs": 232324,
  "shared_gap_pass": 4796,
  "shared_span_pass": 2405,
  "compatible": 2399,
  "new_branches": 20,
  "prior_branches": 84,
  "retained_domains": 2342,
  "minimum_frame": "8442028677986126589157/1048576000000000000000000",
  "minimum_pair": "32992055894668884928258784247/4096000000000000000000000000000",
  "minimum_pair_labels": [406, 70],
  "outside": "1610897/200000000",
  "low_low_margin": "905814668884928258784247/4096000000000000000000000000000",
  "outside_margin": "1/200000000",
  "target": "100681/12500000",
  "proportion": "66812491/99194552",
  "no_new_Lean": true,
  "original_continuous_admission_retained": true
}
```

241个原YA值逐个重算；39直接patch与胞17四个闭g0区间恰覆盖所有低于ell=805094/1e8的40胞，201旧YA均付ell。
425新目录点及旧541点均匹配原2196 PTL的point/pack/list和REG；所有新增query/anchor整个扩展区间处于原已认证convexity region。
旧enabled anchor只在其原有效区间内重锚，无新kernel sampling或曲率假设。
独立482²几何枚举保留原六个共享gap、15共享span、全部闭Floyd/θ约束；结果与2399物理域一一相同。
十新域与47旧替换域互不重叠；各total-span闭分支首尾相接且并集为原闭区间；empty只能由负diag证明。
每个33/42变量矩阵都按物理span共用同一square列，全部[0,1] box、所有残差符号与非负有理λ均收费。
1194正frame乘子、810正新pair乘子吻合；730新增tangent确全部在正λ支撑中。

## 3. 连续及整数计数消费

反射不改变BS与26权。任意实际七gap：捕获域由上述proof付ell；其补集由保留strong capture付tau=805803/1e8。
任意八gap：两子帧均捕获则由完整几何及pair矩阵付M；否则以(tau+ell)/2及非负第九跨度square付款。
safe outer与M均严格大于c=805448/1e8；这是全实gap覆盖，整数端点只表示有理闭不等式。
因此从旧all-zero lossless链得到p=66812491/99194552；p−13471/20000=1251/247986380000>0。
最终liminf下界严格超过67.355%，因而67.355%对充分大高度成立；不把liminf=p写成最终每个高度均≥p。
simple指实际ζ临界线重数1，分母全非平凡零点含重数；distinct只由包含关系消费。
累计／dyadic的(0,T]、(T,2T]与原计数桥一致。near、majorant、每span容量≤2、mass<16、pressure B、32dε与8c端项均未改变。
保留所有线外反射对／实重复零点及实际Hermitian whole operator；先固定ε取T→∞，再ε→0。没有RH或pair-correlation新增前件。
短论文没有必要数学修正。新目标尚未有本审查的Lean/Nano/site收据；旧c403形式化不自动证明新目标。

## 4. 两cutoff：相对R的覆盖PASS与未付上界

原source4229–4310固定presentation自然零延拓和非floor零点；4554先选rho，4556再设U^t，4583–4590在1≤t≤3/2统一。
4609–4684每次保持同psi/rho，真实dyad/profile和gamma−nu_j可不同。4434–4477的有限频率预算可预先分配，两个height不合成一个。
source15223–15436逐项提供所用selected counts、r≈1 no-slot inverse、m≈1/2 zero-slot plain与fixed positive capacities。
note450全文保留actual κ=2β*−1及37/50≤κ≤1的条件，不偷用旧3/4 baseline或目标κ代actual反馈。
五个有序补集完整覆盖upper-short、upper-shorter-long、lower-near-one/long、lower-marked、lower-large-plain。
剩core有同presentation的long r_L与short m同时spike；r,m的O(1/logU)端点误差必须在未来uniform theorem用固定buffer并收费。
strict marked widths、原whole-slot供应与自然mask、两个独立height、恢复后全部short/inverse scales及finite derivative closure均保留。
这是对既有R分析输入的source-proof有限cutoff加强；不认证R本身，也不产生新的mixed upper。

独立Fraction给coverage factor8209647083/1500842361≈5.4700262308。
设计g=1/20000时core需chi≥8209647083/30016847220000≈.0002735013115（其它损失之前）。
eta=1e−6下varying-long rawλ至少≈.0002743346449；fixed-central-R0还付A*s+，需≈.0004255815461。
这两者不同于“目标必要整体count节省”3.7952664e−5乘coverage factor所得极限门槛≈.0002076020689／.0003224065260。
旧λ=.00005仅容许整体节省≈8.98838e−6，已经不足；不得把旧单core条件提升为实际区域。
全部51有限代数检查的flags为new_mixed_upper_estimate/count/region/lean=false，范围正确。
尚未付：真实所有r/m/heights/profile/restored scales上的一侧cross省幂、实际κ邻域／物理余行／low／continuation、ArithmeticProbeObligation。

## 5. 结论

新AM联合证书及短论文限定数学PASS，原continuous capture/PTL与既有allzero解析证明是公开引用输入。
两cutoff报告相对R的实际覆盖修复PASS，原σ边界保持；条件预算不作为新count或strip成果。
本审查没有运行Lean/Nano、重新采集旧捕获或网站提交，没有改任何作者源／旧冻结文件／Git。
