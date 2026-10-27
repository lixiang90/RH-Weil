# finite-cover orbit trace：独立 fresh 逆审

2026-10-27；`/root/cover_fresh` 独占输出。仅审 STATE 指定的 whole-cusp residue 准入比较，不恢复 C047、不预建 C048／585，不编辑 STATE、cadence 或 Git。两份最终原稿已完整独立核读，状态为**修后限定 PASS，支持标准／强旧合成0数学轮结算**；本审核仍不代 root 消费。

## 1. 对象、系数与拓扑

独立从 q_c=t、x=t^w 重算：dπ=w t^(w−1)J′(x)dt，而 ω=Σ_(n≥1)a_n t^(n−1)dt。因此单 sheet h=(w xJ′)^−1Σa_nt^n；完整 w 轨道求和筛去 w∤n，恰抵消 1/w，得 T_c(J(x))=(xJ′)^−1Σ_(m≥1)a_mw x^m。∞ 首项为 −a_w z^−2，没有被漏掉的 z^−1 或额外 1/w。exact 参数 v=π^−1/w 的式(6)也独立相符；a_n 与 b_n 不混同。

coarse 曲线先取 Γ 在 PSL2(Z) 中的像，因而 Γ 不含 −I 时不把 SL lift-order 冒充 coarse cusp width。π 有限 branch values 为 0／1728；coarse ramification 分别 e∈{1,3}／{1,2}，不要求 Γ torsion-free。输入是 coarse 上全局全纯 ω，不无声引入 stack 微分或一般 weight／character 模形式。

Ω=C\[0,1728] 的 π1=Z，**不**因有 cut 就宣 simply-connected。环生成元给 ∞ monodromy；whole cusp orbit 被其保持，故求和 T_c 单值。此证明没有把任一 width>1 单 sheet 当单值，也没有假设全 cover monodromy 平凡。

## 2. 端点、符号及 all-source 域

局部 z−z0=v^e、ω=A(v)dv 给 h=A(v)/(e v^(e−1))。最坏端点指数 2/3、1/2 均小于1；T_c 的各 bank 是有限项和，故 jump ν_c=(T_+−T_-)/(2πi) 属 complex L1。复 ω 不满足一般 Schwarz reflection，不能把 jump 改写 Im(T_+)/π。

独立核 contour 方向：slit domain 的内边界 upper bank 从0向1728，Cauchy 给 T_c=−∫ν_c(t)/(z−t)dt。正向 cusp 圈映成 clockwise z 圈 w 次，恰合成一个完整 trace，故 residue 为 −(2πi)^−1∮_CCW F T_c，两个负号相抵给 ∫Fν_c。以 F=z^m 对 exact-v 的 b_mw 再核一次，系数方向一致。端点小圆 ε^(1/e)→0、∞O(z^−2)分别排原子与 polynomial 项，未凭形式 jump 漏补偿。

L_r 为 entire，固定 cusp 小圈上 π 有界；r∈all-S_exp 使原 contour/u 换序绝对收敛，继而 real compact t 与 ν∈L1 付清全部换序。没有裁成 compact source 来让实际 noncompact 405 关系消失。

原费独立核算：|K(u)|≤C e^(1728 u_+)，N>1728 给强费 C[1/N+1/(N−1728)]p_(N,0)。在 supp r⊂[−L,L] 上，∫e^(3456u_+)du=L+(e^(3456L)−1)/3456，正是稿中原 du 费用平方。zero-extension Dlog≥√log2·du；Hlog 与 Dlog 保留各自定义。没有跨 Γ／ω／λ uniform 常数，也未把 C047 正端点必要 lower 复制到一般 complex jump。

## 3. 强旧审查及一处已修正限定

405／584 已给真实 H>0、H∈S_exp、p=(D²−1/4)H 及全部实平移 p_b∈Pan。对 real compact support，M_H(t)>0，R_ν(p_b)=∫e^(bt)(t²−1/4)M_H(t)ν(t)dt。全部 b 为0时对 b 微分再用多项式在实 compact 上稠密，迫 multiplier·ν=0；L1 无法集中于 t=1/2，故 ν=0。这是584§5的强旧直接消费，不是新的正性来源。

固定有限向量 B 的正确对象是 V=B(S_exp) 与 W=span_C{B(p_b)}。若线性泛函 α 杀 W，compact-real lemma 迫 αB 全源为0；有限维对偶给 W=V。再因 Pan 是含全部 p_b 的复线性子空间，B(Pan)=V。于是同 B 后处理若把**全部 Pan**送同一 base／zero值，或对加入任何 Pan 都不变，便在 V 常值。仅逐点杀每个 p_b 不足以推出非线性情形；不得省略线性组合／完整关系条件。

强旧原稿的 finite-measure 例外、doublepolezero 域、finite 向量、finite族 exact下降与未逐层下降的 D′ family 均已逐项核过。其 compact-real finite-order distribution 旁注只复用 standard Fourier-Laplace uniqueness：q=(t²−1/4)M_H 有两个 simple real zeros，qμ=0 只保两个δ而不保其导数，不是新算术输入。

实际发现并已由原作者修正一处限定：infinite coordinate family 的 finite-projection结论只给 **product/subspace 拓扑密度**；“连续 postmap 在 dense Pan像取同一 y0，则全像常值”还须目标 Hausdorff，或至少 {y0} 闭。修后稿§4已明确，不把有限维 exact像等式搬到无限强拓扑。source-adaptive masks 也已限定为真的保留 finite B 之外数据才未覆盖；仅依 B 选 mask 仍为同一非线性 postmap。

## 4. 消费范围与计轮

transport 原稿建议0数学轮：实际差异是 width>1、复 ω、多 cusp 的局部 trace 运输，所用步骤均为584 slit-Cauchy与标准有限覆盖求和的直接合成；kill-Pan 后果与有限维像结论已被强旧蕴含。它可作为阻止换 level／cusp／mask 重试的具体准入证据，不能冒称新独立 primitive／mixedRR、经典完整 signed成长／core／coupling／Ξ、whole4/5 改善或 Goal 完成。

范围固定 finite modular coarse cover、全纯 ω、whole cusp 固定复 mask、all-S_exp 实际 residue。不包括 meromorphic ω 额外 pole、非whole sheet 数据、额外 relative／非residue source、真正不同的源适应数据、complex／unbounded spectrum。D′ 正逼近中间层无需逐层消 Pan；各 fixed member exact下降失败不推出未逐层下降的 family 极限失败。本审核不补这些缺失前件。

## 5. 下一 joint tower 准入的范围评语

强旧稿§7新列的是实际完整 all-d 公式 B∞(r)_d=CT(L_r(j)g11(q^d))=Σ_(k≥1)c_g(k)a_-dk，并非挑一个新 level 找正例。这给一个可改变“无限目标能否被 finite-prefix 门排除”判断的具体拓扑／反演比较，故可作为**下一单次准入比较**；尚未在本审核执行或消费。

c_g(1)=1 的 formal Dirichlet inverse 与583的 all-radius 超几何衰减是旧输入。下一须核 absolute interchange、固定 rapid-geometric sequence topology 中双向连续及 actual degeneracy differential 的因子 d；若只是 raw 负系数的坐标重编码，就0轮止，不准新 primitive／RR合同。强旧稿已保留其 Pan 强商尚未结算：finite-prefix像等式只给product密度，不能推出强序列拓扑 Pan闭包全吞；标准 finite-principal-part 商与 actual physical Pan商也不能合并。period／dessin只列为未证例子，本审核未消费额外拓扑运输。

## 6. 最终核读版本与结论

* `orbit-trace-transport.md` LF SHA256：`03f14ba2c6693322d710198e2d0ad08d5c21efb062b49934ac08cb1da924d51d`；已完整独立核读。
* `old-consequence-and-repairs.md` LF SHA256：`1cdfcd77f6d194c2d4ef1188b561cb57e23939562072d332525c2a79ad64b0cc`；含已核目标分离性和same-B adaptive限定修正，以及未执行的joint-tower准入范围。

最终限定 PASS：whole-cusp transport与强旧全部前件在上述版本闭合；建议统一保存0额外数学轮，cadence不动。没有新经典正性／独立primitive／mixedRR、whole4/5 UPPER或核心瓶颈移除，长期 Goal 完成门仍 open。root须核最终消费范围／版本后自行结算；本文件不修改cadence、不授予任何新执行范围。
