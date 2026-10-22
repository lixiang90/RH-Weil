# C037／574 整体独立 fresh：实际 clutch、源运输与容量范围

2026-10-22。新的独立审查 task；不是先前 actual-cover 稿的续写或自我结算。
本稿只写此独占报告，不修改原稿、STATE、cadence 或合同。已读当前 STATE、C037，
[574](../../../notes/574-actual-adelic-cover-relative-picard-and-source-transport.md)、
[periodic 原证明](periodic-clutch-classification.md)、[边界比较](boundary-cover-and-existing-lines.md)、
[原费控制](source-norms-and-controls.md)及[adversarial 报告](clutch-adversarial-review.md)，并定点回查413、405和上一模块门。
Goal／固定基线仍 G20261014／0c4f；此处不由文本、hash或工具结构检查认证数学。

## 1. 限定结论

**限定 PASS。** 未发现需要阻断消费的数学缺陷。
实际413双位开覆盖上，指定 transition 子族 \(g_z(x)=e^{zx}\) 的完整 base-fixed 等变同构核、
两边界既定 frame 的相对核、以及 Γ 不变连续非退化正度量门均有完整证明。
405全主关系和537非根在同一 source recipe 上已实际检验；合法 nonlinear Q-marker 也保留，未以失败子类冒充所有源 map 不存在。
完整经典型的 Γ、所有 proper powers、双 pole 和复混合系数未删。

允许消费的新增量，是这一个实际指数 clutch 子族的精确 kernel／relative kernel／invariant metric 判据。
它不是整个 Picard 群的分类，不是函数域意义 degree-zero 已实现，不是新的正极化、RR容量或经典RH输入。
本轮 source-transport 所试的简单候选在用户停止门处收口；长期宏观瓶颈未变。

## 2. 对象与覆盖确实是原实际几何

413给 \(T=\mathbb Z\cup\{\infty\}\)，上尾收敛到∞；
\(Y=T^2\times\mathbb R_t\)，\(\Gamma=\mathbb Z^2\) 作用为
\((a,b)(j,k,t)=(j+a,k+b,t+aL+bM)\)。
\(O\) 删双∞层，\(W_p=\{k\in\mathbb Z\}\)、\(W_q=\{j\in\mathbb Z\}\) 确为 Γ 不变开片并覆盖O。
共同交 \(B=\mathbb Z^2\times\mathbb R\) 的 \(x=t-jL-kM\) 是同一个坐标，未对一边倒置方向。
两边 proper 后的实际 side quotients 分别为螺旋加圆的 \(Z_L,Z_M\)；全O非proper。
本轮没有将整个 quotient 误换为 Hausdorff proper orbit space。

每边上的指定线具有 trivial fiber action，因此 base-fixed Γ 等变同构的系数恰是各 side quotient 上的连续单位。
这是 kernel 必要性证明的足够覆盖；无需假设所有等变线均能由此构造。
线在O上的普通continuous clutch与非交换 crossed-product 的有限支投影是不同对象，文中没有混同。

full adelic character 线作为标准来源对照，也明确区别 additive adele 与 idele 拓扑。
原费稿当前§1已将先前“idele开部分”改为 idele限制端，并明确不是open immersion；adversarial所要求勘误已落地。
它不改变本轮 \(W_p/W_q\) 是真正开覆盖的证明。

## 3. 精确子族分类的重算

对side单位a，紧负尾加边界圆给周期边界值A，且 \(a(x)-A(x)\to0\) 在整个负尾一致成立。
证明只需取坏点列、在圆相位上取收敛子列；其极限都为同一边界点，产生矛盾。
边界单位在紧圆上无零，又给负尾正上下界。这一步没有偷加正端有界性。

若 \(e^{zx}=a(x)/b(x)\)，模的上下界先迫 \(\Re z=0\)。写 \(z=i\lambda\)，
则 \(e^{i\lambda x}-A(x)/B(x)\to0\) 于整个负尾。
紧三频环面有无界正近回归序列 \(t_n\)：若任意精度的近回归时间不能取无界，
有限个候选中的一个便为精确周期，其倍数又给无界序列。
将负尾式作用于 \(x-t_n\)，三频相位同时归1即得处处恒等
\(e^{i\lambda x}=A(x)/B(x)\)。

周期无零函数的绕数分解给
\(A=e^{2\pi imx/L}e^{a_0(x)}\)、\(B=e^{2\pi inx/M}e^{b_0(x)}\)，有界周期log存在。
剩余连续 \(2\pi i\mathbb Z\) 值函数恒定，有界log迫线性频率系数为零。
所以absolute核准确为

\[
 i\Lambda,
 \qquad\Lambda=(2\pi/L)\mathbb Z+(2\pi/M)\mathbb Z.
\]

逆向直接由两个周期单位延拓获得，故不是仅证明一个必要条件。
对任意z,w取差便给574(2)。\(i\pi/L\notin i\Lambda\) 由 \(L/M\) 无理保证；
其两倍在核内，因此所称absolute二阶非零类也准确。
无理性只用不同素数幂唯一分解，不含未知零点信息。

必须保留的范围是：这里只分类实际固定O上、同构覆盖恒等映射的该指定子族。
\(\mathbb C/i\Lambda\) 只取自然参数商，不是整个Pic的集合或拓扑分类。

## 4. Relative双frames、度量与非proper同伦

保留P、Q上既定frames时，允许gauge的两负尾边界值均为1。
故平凡化要求 \(e^{zx}\to1\) 于负无穷，精确迫z=0；对两参数取差即得relative核0。
只要求边界限制可平凡、而不固定frames的对象仍按absolute核识别，原稿已明确，未偷换两种relative含义。

Γ不变正Hermitian metric在指定两片frame内下降为 \(Z_L,Z_M\) 上正连续函数。
两紧圆的正上下界，与metric compatibility的比值 \(e^{2\Re z x}\) 相比较，必要地迫 \(\Re z=0\)。
反向两side取metric1即闭合充分性，且boundary frames均为unit长度。
这不是底层O没有普通正metric的声明；非不变、边界退化、奇异或加权方案均没有被此定理排除。

\(s\mapsto e^{szx}\) 确给一个实际等变continuous族。
它不与ordinary paracompact Hausdorff底空间上的line同伦分类冲突：这里改变的是非proper等变范畴，
不是证明ordinary底层line同伦不变性失败。原稿保留了这一层次。

## 5. 405全主关系、537及一般线性标签

405真实正函数h给 \(H=e^{u/2}h>0\)，实际principal为
\(P=e^{u/2}(D^2+D)h=(D^2-1/4)H\)。
原 \(S_{\exp}\) 衰减允许所有分部积分，因此

\[
 \mu_\pm(P)=0,\qquad \int P=-\tfrac14\int H<0.
\]

于是mean标签把零源商类送到非平凡实参数线，absolute和framed门都失败。
相位mean虽有不变metric，缩放同一P可得到 \(i\pi/L\)，故也有明确非平凡principal像；
没有犯“任意一个纯虚非零参数都非平凡”的错误。
degree-only参数消全部Pan，却把537双degree零的 \(r_0=(D^2-1/4)\psi\) 送零。
此r0非零，旧537完整型正性给实际nonroot；mean看见它，不能与另一个标签消关系的优点拼成同一成功候选。
405的h不是Pan，其双degree \((1/4,1/4)\) 保留，未将全I误删。

复线性标签消全部Pan的absolute类，只先推出 \(\ell(P_c)\subset i\Lambda\)。
Pan对所有标量闭合，非零 \(\ell(q)\) 的标量倍不可能包含在可数集合中，故真正得到 \(\ell(P_c)=0\)。
随后若标签本身在全线du/Dlog连续，才可由553稠密性推出零标签。
这条证明没有把非Hausdorff参数商当作Hausdorff目标套用旧定理。
Fréchet、变域、nonlinear、付费cofinal及新的relative几何逃逸保持。

Mellin试验式 \(\ell_z(P)=\frac12(z^2-1/4)\xi(1/2+z)\) 与405的 \(M_h=\xi/2\) 相符。
单evaluation的修补回双degree或旧完整谱坐标；它不是一般有限组合都不可能的分类。

## 6. 合法Q-marker确实必须保留

\(z(r)=icQ_\zeta(r)\) 合法且不读取未知零点位置：既定完整分布型Q是实Hermitian型，
405的完整identity使Pan成为其radical，故所有principal coset被消去。
选 \(c=\pi/(LQ_\zeta(r_0))\) 使r0映到明确非平凡 \(i\pi/L\)；纯虚参数也有Γ不变正纤维metric。
所以不能把本轮结论写成“实际源map不存在”或“四项门不能同时通过”。

但此marker把欲比较的原Q数值直接放进参数，没有独立容量信息。
它不把source加法送tensor：令 \(a=r_0/\sqrt2\)，则 \(z(2a)=i2\pi/L\) 在absolute核内，
而 \(2z(a)=i\pi/L\) 不在核内，原稿的反例是准确的。
framed范畴更直接保留这两个不同参数；并未通过任意gauge使它们相同。
不能从unitary fiber metric反推数值符号，因为正负Q都生成纯虚参数。

## 7. 原域、原norm和成长量词

\(\ell_0\) 在先fixed support \([-A,A]\) 上的du精确dual norm为 \(\sqrt{2A}\)；
在光滑compact类以近似常函数取sup，边界严格内支撑不妨碍该值。
Dlog的 \(\sqrt{2A/\log2}\) 只作为upper，稿件未报精确dual。
这些mean/Mellin代表费用没有下降为全线quotient费用；全Pan的非compact试验另行保留。

source窗A、cover窗B、有限arrow高度是不同变量。\(e^{B|\Re z|}\) 及 \(B|z-w|\) 只是给定frame/图表费用；
纯虚不同频率在整个R的uniform距仍为2，compact-open参数连续不能升级全bulk乘子norm连续。
稿件没有把某个坏frame或ambient最坏逆的费当所有actual lift的必要lower。

Q-marker在每个先fixed A上有 \(|Q(r)|\le C_A\|r\|_{Dlog}^2\) 及极化差界：
完整Γ的log乘子由Dlog付，有限窗素数幂shift与rank-two pole是有界扰动。
这是旧full-form结果的实际消费，不能改报纯du同级界或uniform成长C_A。
完整Γ在高频增长，故保留Dlog责任是必要的。未得到原源到算术section/metric的全域有费比较。

## 8. FullQ系数与两个控制的独立核对

令 \(k(v)=e^{-v/2}/(1-e^{-2v})\)。
digamma积分差在变量 \(w=2v\) 后给

\[
 \Re\psi(1/4+it/2)-\psi(1/4)
 =2\int_0^\infty k(v)(1-\cos tv)\,dv.
\]

而 \(\|\tau_vr-r\|^2\) 的Fourier乘子是 \(2(1-\cos tv)\)。
所以574(7)的 \(\frac12\int 2k(v)\|\tau_vr-r\|^2\) 系数正确，
与 \(\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi=2\theta'(t)\) 一致。
contact常数 \(\psi(1/4)-\log\pi\)、finite项的−2和double pole的 \(2\Re(\mu_+\overline{\mu_-})\) 也均保留。
全complex源的real-part、star和mixed极化没有被换成仅实偶对角检验。

连续对照中 \(w^2=-d\)、\(w^\dagger=-w\) 的regular trace给 \(2|A|^2+2d|B|^2\)。
取 \(g=u\phi\)、\(r=(D^2-1/4)g\)，奇性给mean零，分部积分给 \(a_r=-(d+1/4)a_g\)。
\(B_g>0\) 对 \(d=\pm1/16\) 均成立，故 \(Q_c(r)=2d(d+1/4)^2B_g^2\) 严格异号。
mean漏掉两段，Q-marker则两号均unitary；这项控制没有给连续模型虚构经典adeles。
其Γ=0是本身指定背景，未从经典预算删Γ。

函数域已付真实genus2控制也准确：\(K\sim2\infty\)、\(D=P+Q\)，canonical评价矩阵det1给 \(h^0(K-D)=0\)。
RR给 \(h^0(D)=1\)，而 \(h^0(K)=2\)，所以 \(L_0=O(D-K)\) 非平凡；degree0非平凡线自身 \(h^0(L_0)=0\)，
有效化后 \(h^0(K\otimes L_0)=1\)。这是旧proper曲线上的控制，未被冒领为当前continuous clutch的section theorem。
proper族/base change和Picard校正overlap来自既有曲线几何；尚未运输到实际adelic新线。

## 9. Root消费、计轮与停止的准确边界

没有数学BLOCK项；必须在最终消费中继续保留以上对象、norm、relative frame和nonHausdorff前件。
源标签已通过或失败的门要逐候选表述：
decaying clutch全部平凡；mean保r0失败Pan；degree-only消Pan漏r0；Q-marker两门俱过但为旧数值包装。
本轮不能撤销这份最强合法repair，再以更弱候选失败申报方法不可能。

另已读取[574结算草稿](../../../goals/reviews/2026-10-22-actual-cover-relative-picard-574-settlement.md)：
其新旧扣除、cadence2→3一次、宏观瓶颈未变及唯一重新准入条件与本审查一致。
它没有从“非平凡line”推到算术degree-zero或独立容量，也没有将来源稿和审查各算一轮。
periodic§7最新修订亦已核：单Mellin／zero-jet标量只读一个旧商坐标，全部必要jets的joint忠实性归519/520，
未再将单scalar称为忠实整个商。以上两项不改变主kernel证明或本限定PASS。

periodic kernel／framed kernel／Γ-invariant metric判据是一个实际新完整研究结果，
按C037统一一轮结算合理；标准full-stack character构造、旧费用、controls、审查和推送不各自计轮。
该局部几何结论没有消除源桥到同一整模型的valuation／有效截面／mixed容量责任，
也未改善strong-old542+555→557的whole leading4/5上预算、actual core/coupling/Ξ或Goal完成门。

按用户stop rule，当前mean／decaying／旧谱或Q数值重新标line的recipe应停止，不续scalar/probe/frame参数。
下一准入需要实物：区别于Q-marker的relative Cartier／valuative源数据、全Pan实际同构、537和连续符号控制、原域费用，
并至少一项独立过滤/有效性/截面容量设施；不能把未知RRidentity换名称另开合同。
这不排非标量、新relative层、强拓扑、变域或有费无限传递。

**最终审查意见：限定 PASS，可 root 按上述前件闭合后消费574；宏观瓶颈未改变。**
