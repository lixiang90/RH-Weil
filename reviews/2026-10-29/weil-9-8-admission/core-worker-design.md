# 固定9/8：新有限比较 core worker 实现范围

2026-10-29。限定实现与prepare-only，没有运行trial、矩阵compiler、Gram proposal或残差验算；没有改STATE、cadence、Git或Goal。独占新原创程序是 `scripts/weil_9_8_core_pilot.py`；它不导入上游程序、不复制上游完整模块，全部实际数值/manifest/receipt留ignored `literature/local/2026-10-29-weil-9-8/pilot/core-run-02/`。

## 1. 冻结配置与当前实际产物

采用已给新inverse原件 `new-inverse-threshold-admission.md`（SHA256 `e60800f4b36e737d3bd13efa0bd57bcd0d799a79ac81a0e9313f20b73450af42`）的同一参数：L9/8、Ω256、N448、μ1/8、m15/64、b433/64、r2^-85、p2^-440、θ2^-48、χ1、α0=2^-122、β0=2^-22。Trial固定110 decimal digits、Z的2^-256格；Gram固定256 decimal digits、factor的2^-512格、normalized diagonal shift2^-480。无L/weight/μ/θ/degree/precision搜索。

| 当前绑定 | SHA256 |
|---|---|
| 新core worker | `d9ac746c3d56199ea65385f9883390c19a64b06ba8397f52ad96201d20485961` |
| ignored core manifest | `5974885eba88831106d3395adf908f73a8c3180671457a7233aff3e44d2b239f` |
| canonical core configuration | `c315a040c3412694f7010f81131d76c4ac808cef9e19a7b0214bcc9d3c86d290` |
| source worker | `7589b854cbcd2f1c2fcdf0ecce60b614af7e1d73992b6f64719e1624a0ad0961` |
| source manifest | `15ae30f087481a40d9c9d6bf3ff517ea1e50aba04b3899fcdd049c55364511e4` |
| source configuration | `8e4e59c11469cf35e5ad2e85a433660e6720ebd322d7ffd5c87d805cf2c0d364` |

实际执行只到prepare metadata。第一版877f…的prepare保存在`core-run-01/manifest.json`（SHA e7ec…），没有科学stage。终审静态读原08/07发现source rows实际为upper triangle `i=0…447,j=i…447 step2`，第一版reader错误按lower解释，若运行会无谓NONPASS；尚未运行即发现并修正。没有覆盖或删除旧manifest，当前代码只把reader改为actual upper顺序，并把独占目录改为core-run-02，数学/精度configuration SHA完全不变。随后再执行 `prepare`生成上表新manifest，返回 `CORE_PREPARED_NOT_EXECUTED`。这两次只读固定hash/写元数据，不读源数值packets、不调用科学函数，不是两次数值尝试或参数搜索。没有core科学stage receipt、factor或目标矩阵。此文记录实现，不能代独立codefresh/root准入。

## 2. 入口、绑定与保存失败

唯一入口为prepare、isolation-test、trial、compile、gram。运行强制 `-I -S -B`、assertions，且每个非prepare stage都须显式传当前worker和manifest两个SHA。prepare拒绝已有core-run目录；科学stage拒绝既有packet/receipt/failure/access输出。输出采用exclusive create，任何失败保留先前产物与NONPASS错误、traceback和access record，不自动重试或改参数。

运行中精确输入/输出路径allowlist、标准库范围，拒绝socket/process/ctypes与未知descriptor。所有原输入hash在开始及完成重核。isolation-test不要求源数值完成，只做外部read/socket/subprocess三个拒绝控制。此为Python audit hook，非OS syscall sandbox。没有导入带toplevel dispatch的原run/stage/scalar或任何原core模块。

科学stages先验source三个receipt：同一新worker/manifest/config、SOURCE_ONLY_NOT_FULL_Q、output SHA、1024 moments/1152bit/trueθ含Binet一次、15shift/225pairs/151200 intervals、896 tail coordinates、相应全部control数量。矩阵的moment SHA链、新raw matrix256-bit scale、tail640-bit和9/8配置再核。每个core后继stage还核前一stage的packet SHA、相同core worker/config，以及前一stage全部输入hash与当前输入一致。两个parity sector使用原Legendre degree `q_i=8(2i+1)`，各224维。

source-only的成功receipt不付解析费用；所有core输出继续 `fullQCertified:false` 并要求root关闭analytic premises。最终即使finite sign通过，也仅发 `FINITE_STAGE_PASS_NOT_FULL_Q`，没有RH/full-Q PASS入口。

## 3. Trial及inverse整数

从独立source intervals的endpoint sums取raw中心a,b,j，分母S=2^257；按source实际upper顺序读全部50400项，并对称扩到448×448，异parity位置明确为零。完整tail midpoint integers分母2^641。输入全量读顺序、维数、区间、proper parity和caps均检查；不接受单子块替代完整source。

Trial只解一次

    Q(8b−a)Q ·(Z/R)=8Qa−18S I，R=2^256。

110-digit Cholesky/forward/back substitution只提议Z，failed decimal pivot记录inconclusive，不能推任何数学负性。Z各项cap2^272；完整actual `ν=Σ q_iq_jZij²` 重算。自适应量只有据该ν取得最小整数k≥0使 `ν≤2^(512+2k)`，令y=2^k≥1；k≤37。它是已产生同一trial的确定上包围，不是参数搜索，不继承旧y=8。

Inverse整数按已给恒等式构造Cw=2^769、c=8Cw+(9y²+16y)2^549、F及V。以u=QZ独立形成u*au/u*bu、au的线性项；V的全部entries对称、每列可除对应q_j及F/V caps逐项实际检查。W≥G>0与congruence正性仍来自root消费的一般inverse/math证明及本次source误差/norm前件，不能由目标sign倒推。

## 4. 两个完整compiler

采用同一已重导λ0和六个整系数：cJ=9·2^1025、cU324、cΓ=162·2^1282λ0、cB=9·2^1003、cAA=2^745、cW=2916·2^2051；系数Fraction清分母须精确为整数。没有原607630911、1309或旧3353-bit scale。

Direct实现六项独立contraction `VjV, VQ^-1V, VbV, (aV)*Q(aV), (Vt)(Vt)*, V`，采用row/column dot product累计。Combined实现另从aQa形成Hinner，再算Yv Hinner Yv*+cW V；aQa和matrix products采用不同k-major逐项累加顺序，不调用direct compiler或借其intermediates。两路必须逐个比较224² entries、目标对称及3200-bit cap。正congruence是原件的

    K=T0·18²Cw² Bc*P0 Bc，T0=9·2^1282>0。

程序绑定该数学原件，但字节/两compiler相等本身不证明congruence的语义；root/fresh仍须审对象、系数、正号与原norm运输。

## 5. 单次Gram proposal与exact sign

每sector从actual K整数绝对值取得一次bit scale b，提议normalized `K/2^b−2^-480 I`的Cholesky，固定256digits；把L量化到2^-512格给整数F。实际scale只是同一目标的确定归一化，不是增精度/参数扫描。

exact checker逐entry重算

    Rcert=2^1024 K−2^b FF*−2^(b+544)I，
    d=2^(b+544)>0。

所有224行的 `Σ_j|Rcert_ij|<d` 才付该sector严格正号，real F的Gram对complex向量同样PSD。结果保存完整F、全部row sums、b、clearing/Gram/diagonal powers；不是只核浮点pivot或少量rows。成功后另把F00增加2^600，调用相同残差检查器，须实际拒绝。该control在首个失败row可提前止；真实证书总是全行核完。

若Decimal Gram在pivot i不正，只从已生成leading Cholesky提议一个量化有理方向v；用**原K**精确计算v*Kv，保存numerator/denominator。仅当此数为负才标actual finite target negative；这仍不是full-Q负方向。若exact residual不通过，保存当前factor/rows和NONPASS；不改shift/精度/μ/N重试。首sector失败会停止当前stage，不把未执行另一sector叫已核；所有先前完整trial/compile输出保留。

## 6. Root下一步及仍未付事项

Root先独立审此worker/code及新inverse/congruence语义，并确认实际source三个stages已全量成功，再决定是否执行本固定core尝试。顺序isolation-test→trial→compile→gram，每步同两个SHA pins；两个sectors都通过才有全部448-mode finite comparison。当前没有执行这些stages，不声称其运行耗时或成功概率。

全解析域、Γ/contact/properpowers/双pole、δ/rank-two、576 kernel/Binet一次、完整cross/complement/source误差还须同root premise-closure消费；finite criterion成功之后才可能回到原Q≥δ/16。固定窗净增和成长/RH核心primitive/principal/mixed瓶颈继续分开。本文不计数学轮、不完成Goal，也不自行授权numeric运行。
