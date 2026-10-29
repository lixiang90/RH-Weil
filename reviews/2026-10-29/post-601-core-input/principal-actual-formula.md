# 一份实际 framed Hecke 源公式：整完成除法精确回到旧源商

2026-10-29；`/root/post601_principal_actual_formula` 独占原稿。**没有得到可准入的新独立 principal/mixed 输入。** 本次只设计并检验以下一个具体对象：以405真实Gaussian的整Mellin函数作分母，给复杂曲线上的局部rank-two lattice modification；其regular-gauge关系先独立定义，再测试405/Pan和537非根。保外部frame时，完整源信息恰回到519已付的全重数jets商；忘掉frame时，这条全局亚纯上三角规则把所有源的底层bundle一并平凡化。不能把这两个角色混成“新principal桥已经建好”。

这不是调整旧rank-three连接的矩阵尺寸、Green核、端框架或参数。这里的变量是复Mellin平面、离散谱除子上的局部O-lattice及指定外部frame；旧连接则在physical log线演化。实际比较后，本候选仍然没有越过更强的519/520旧资产，不作为新算术来源或新方法类边界计功。最终消费/计轮由root决定，本文不预授C065/602。

## 1. 恢复和执行边界

实际读根AGENTS、README当前入口和STATE，执行`research_state.py check`后`show`，结构检查通过；读完整G20261027、停止的C064、D20261029AJ及宏观前沿当前601摘要。恢复到0c4f基线、solecadence3/history65/latest601/formal20、三Goal门open。父现场已经重核同runtime1793085111 active和最终219a7aa；本子稿将其作为父观察，不冒称本子任务独立调用了父Goal/GitHubAPI。工作树实际为root更新STATE及本轮新目录，未覆写它们。

没有重新列573–584库存，没有读新paper、网页、原PDF、作者后章或引用链，没有数值/大证书/模型参数测试。一次拟派的只读局部coset检查因agent thread limit未启动，无文件/结果/待续handle；以下全部有限代数由本稿直接核，不以该失败充作独立审查。只写本文件，不改STATE、cadence、Goal、文献库、合同或Git。

## 2. 唯一实际公式与独立的局部关系

仍以r表示physical复源，r∈S_exp,C；raw源为f(u)=e^(−u/2)r(u)。两者在这一个全指数Fréchet空间之间为明确连续线性同构。定义

    F_r(s)=M_f(s)=∫_R exp[(s−1/2)u] r(u)du，
    µ_+(r)=F_r(1)，µ_−(r)=F_r(0)。                         (1)

F_r整，固定闭实部带上的虚方向快速衰减。分母不是未知零点的猜测或一个按Pan命名的理想，而是405实际源给出的完整整函数：

    η(x)=πx²(πx²−3/2)exp(−πx²)，h=Eη，
    H0(s)=M_h(s)=ξ_Riemann(s)/2，H0(0)=H0(1)=1/4。          (2)

H0的零除子D在C上局部有限，零点恰为通常ζ非平凡零点，阶数保实际mρ；不假设RH、简单性或spacing。虽然(2)可直接通过Gaussian/Mellin定义而不先求零点位置，使用它的零除子仍是在使用旧ζ谱对象，不是一个独立构造的正几何谱。

取曲线X=C、U0=X\D。在每个ρ的小圆盘Uρ上，以Oρ表示holomorphic germs、Kρ表示meromorphic germs，固定外部平凡化于U0。写

    g_r(s)=F_r(s)/H0(s)，
    T_r(s)=[[1,g_r(s)],[0,1]]，
    Lρ(r)=T_r Oρ² ⊂ Kρ²。                                 (3)

这给实际自由rank-two局部O-lattice与外部frame的modification数据。每个紧集只有有限处需要处理；不把D的无限支集当成P¹上的有限代数除子，也不默认在∞具有meromorphic延拓或有限arithmetical height。detT_r=1，所以其普通determinant line在这里有显式平凡化；尚未给一个有完整Weil曲率的metric。

关系不是“把Pan的像叫boundary”。先采用标准局部规则：两个这样的lattice在固定外部frame下相同，当且仅当右乘差属于GL2(Oρ)。本规则下

    T_r^(−1) T_t=T_(t−r)，
    Lρ(r)=Lρ(t)  ⇔  g_t−g_r ∈Oρ。                          (4)

方向为右coset，因为L=T Oρ²；不能把左/右coset或忘frame后的bundle同构混用。由上三角矩阵及其逆可逐项验证(4)：差矩阵的唯一非正则候选entry就是g_t−g_r。

等价地，保留的局部坐标是

    ppρ(g_r)=Σ_(k=1)^mρ A_(ρ,k)(r)(s−ρ)^(−k)。             (5)

这是additive principal-parts对象，不是整数Cartier除子的系数。局部relative position有其整数pole order，并不使源的连续Laurent系数、双端µ值或某个complex加权cycle自动成为同一个算术整线丛。

在保双端标签的版本中，唯一source map为

    D_r=(µ_+(r), µ_−(r), {Lρ(r)}_ρ)，                       (6)

在这个上三角orbit上以(5)的加法读出。实际source image由(1)–(3)给出；没有声称它等于无约束的全部principal-parts乘积。

## 3. 全重数与405真实Pan首检

令H0(s)=(s−ρ)^m hρ(s)，hρ(ρ)≠0。则

    A_(ρ,k)(r)=[∂_s^(m−k)(F_r/hρ)](ρ)/(m−k)!，1≤k≤m。     (7)

这些坐标是F_r在ρ的0至m−1阶jets的可逆三角变换；主对角为非零的1/hρ(ρ)。因此

    ∀ρ: ppρ(g_r)=0
      ⇔ F_r^(j)(ρ)=0，0≤j<mρ，∀ρ
      ⇔ f=e^(−u/2)r∈I。                                  (8)

最后一个等号恰是519的实际源闭像I=J=R_jet，不能改成仅值零的516 R_val。这里没有新的Mellin除法或谱综合定理：它们已由518/519付清。加上(1)两个µ标签后，kernel(6)精确为C(P_an)，只是405/519已付商的又一具体呈现；这不是要求任意新几何必须有这个kernel。

405真实关系p=(D²+D)h有

    M_p(s)=s(s−1)H0(s)，c(p)=d(p)=0。

令P(u)=e^(u/2)p(u)，以及全部physical平移P_b(u)=P(u−b)。则

    F_(P_b)(s)=exp[(s−1/2)b]s(s−1)H0(s)，
    g_(P_b)(s)=exp[(s−1/2)b]s(s−1)                         (9)

为整函数。因此每个真实P_b的所有Lρ均为标准lattice，两µ为0。它不是compact crop、不是只核一个平移，也不是用boundary定义倒推。对一般C(P_an)，(8)给相同结论。

双端标签不能省略：φ=e^(u/2)h满足g_φ=1，所以全部局部lattice标准；但µ_+(φ)=µ_−(φ)=1/4。若只保(5)并把其kernel全部视为principal，便把405已明确的非双degree零源也消去。此处不再把这个旧缺陷当成新反例。

## 4. 537非根确被frame保留，但其信息早已支付

取0≠ψ∈Cc∞((−17/16,17/16);R)，r0=(D²−1/4)ψ。r0非零、仍compact smooth，分部积分给µ_±(r0)=0。537已支付的完整Q_W严格正性给Q_W(r0)>0；不重放原证书或将它升级成长。

若全部Lρ(r0)标准，则(8)给f0=e^(−u/2)r0∈I，再由双µ零给f0∈P_an，405完整配对根关系使Q_W(r0)=0，矛盾。故至少一处principal part非零，frame版本确实没有把这个非根丢掉。

然而这一“消Pan、保非根”只证明(6)忠实表达已有源商的相应信息。更短旧链已经是519实际jets闭像→520全Fréchet谱/Jordan重数→553强拓扑/成长费用。没有新增独立的算术有效性、sections lift、mixedRR或正极化；把旧ξ谱除子改成lattice modification并不付款。

## 5. 忘外部frame时的显式平凡化，而非principal成功

(3)还可在U0与各Uρ的cover上当成holomorphic transition matrix。为固定箭头约定，设局部坐标满足

    v0=T_r vρ   on U0∩Uρ。

T_r在U0上holomorphic且可逆，T_r^(−1)也是。改变U0坐标为w0=T_r^(−1)v0，保wρ=vρ，则交上w0=wρ，得到整个底层bundle的显式平凡化。这只使用本候选已经全局给出的g_r；不调用“所有principal parts都可解”的Mittag–Leffler存在定理。

但这个改动改变了U0上的指定外部frame。如果frame是(3)的数据之一，不能这么消；如果候选principal商允许这个外部holomorphic gauge，则对**每个r**都能这么消，包括上面的537非根。用(9)通过Pan门后再忘记frame，并不能既消Pan又保非根。

相同地，若把(5)再商掉所有全局meromorphic function的principal parts，当前每个g_r本来就是全局meromorphic函数，所以所有候选类立即为零；无需证明这个全局pp映射对任意目标数据满射。不能把raw principal part、framed lattice orbit、无frame bundle class、全球meromorphic principal商四种角色合并。

此处只裁决一个已明定的全局亚纯上三角规则，不排所有Hecke modification、非分裂extension、其它曲线、∞处指定增长/metric或独立算术sheaf。那些是不同输入与允许gauge，本文没有构造或授予后继预算。

## 6. 原范数、实际配对和coverage仍未支付

(7)逐坐标在原S_exp拓扑连续。对α=Reρ−1/2、N>|α|，

    |F_r^(j)(ρ)| ≤ 2j! p_(N,0)(r)/(N−|α|)^(j+1)。          (10)

需要(7)的hρ局部导数及1/hρ(ρ)系数；没有任何all-height、all-jets或source-family共同上界。不能从source source-map合法推出joint范数或自动闭image。

在先fixed支集[−L,L]的全complex L²源上，F_r^(j)(ρ)作为单一读出的精确squared dual norm是

    ∫_(−L)^L u^(2j) exp(2αu)du。                           (11)

它是553已付费用：critical为2L^(2j+1)/(2j+1)，fixed offcritical有指数增长；Laurent坐标另乘(7)的实际系数。本文不冒称global du有界，因此没有误用553的dense-du零读出定理；但允许强拓扑并没有产生新的独立符号或共同成长控制。原zero-extension Dlog、Γ/contact、全部proper powers/双pole及joint coverage不能从(11)单坐标自动取得。

516/553的完整Hermitian目标使用实际partner 1−conjρ，不能拿各|A_(ρ,k)|²的PSD和替代。Higher principal-part coefficients携带Jordan jets，而完整标量Weil型只用零点值及重数权；二者不同。这里既没有新mixed pairing identity，也没有有费canonical metric把该modification的交数等同完整Q_W。

当前最强whole542+555→557仍为leading4/5负惯性UPPER；595同一物理见证的强正点/gap和600/601范围均由root当前恢复，本稿未重算。没有改善principal/mixed/dangerouscorecross/成长Ξ，Goal三门仍open。

## 7. 准入裁决与确切缺失输入

本次三句为：输入是(1)–(3)这一个实际局部Hecke修改公式；测试是独立regular-gauge关系下的405全Pan及537非根，并比较fulljets/source-frame职责；执行后得到frame版本精确等于旧519/520源商，忘frame版本全零，故未得到新独立principal/mixed输入。

建议按**具体公式的强旧/类型0准入止损**保存：不是“只思考未执行”，也不是新完整未知方法类的失败。其全quantifier责任已由519源像识别、520谱和405双degree分解包含，局部上三角coset/显式gauge为标准重呈现，不应因几何名词多计数学轮。最终由root对齐另一独占稿及不同fresh后统一分类。

停止本公式；不更换rank、frame、分母、零点集合、compactification或添加未知metric继续。缺失的仍是：一个与已知ξ谱商不同、源及regular/principal关系由实际算术几何独立给出、能承接同源mixed并有原norm/joint成长费用的对象。没有新具体实物时，不把“在∞加条件”或“另找正metric”当作已准继任，不自动读paper/章节。

本文件为terminal原稿；没有后台或待执行计算。父root须全文读取并独立核实际版本后才能消费；本稿不替root更新状态或计数。

## 8. 实际输入和版本

以下raw SHA仅认证版本。实际阅读：405全文；519/520/553全文；516 §§1–3及§§5–8（其余不作新依赖）；537开头至§4的实际Q定义/固定窗全源statement与域，不重审nested证书；Goal/C064全文，AJ及frontier当前摘要。未以hash表冒称重新审计历史全部proof/source。

| 输入 | bytes | raw SHA256 |
|---|---:|---|
| `goals/GOAL.20261027.md` | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `goals/contracts/C064-haran-integer-affine-fold.md` | 2047 | `765aa6546b77297a475a0003ce6c4a362736915ae36eb014874d3f3d21971399` |
| `notes/405-f1-adelic-restriction-moments-and-radical.md` | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| `notes/516-f1-global-mixed-radical-and-mellin-jets.md` | 9569 | `d21496da1ee280a0f733f322baddf46eb4cac4b50242494ae76b0d464533bbbd` |
| `notes/519-f1-closed-source-image-and-degree-moments.md` | 5766 | `93d39e6d932c9913f5feb77bed4d1ad096c9d984ed571e894576fce6c53b124c` |
| `notes/520-f1-source-quotient-spectrum-and-centered-growth.md` | 6311 | `81a05708dfd2139d374d9fac7f631e66ea4449d502cf9fb0c52f53b900dc9651` |
| `notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md` | 6613 | `35a40c35d1eaa7fafb462361ddef1bfb9643402b5670f832b9142aeb4b74abce` |
| `notes/537-source-exact-weil-window-positive-tail-admission.md` | 8155 | `269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8` |
