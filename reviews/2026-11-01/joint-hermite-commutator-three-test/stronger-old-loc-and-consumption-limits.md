# ROOT消费限制：更强已付LOC、trace与实际主门

2026-11-01；本文件保原三个数学稿字节，不把其draft或conditional结论当ROOT验收。当前限定如下，等待独立终审和统一结算。

## 1. 更强旧前件实际已付，o(j)不作新净成果

已全文核当前需要的旧 localization-and-rate-proof.md §§1–4及其root-consumption-scope.json的LOC/D4，均在reviews/2026-10-29/critical-prime-covariance-proof/。原localization稿14467bytes/SHA3a5c61a0aacdd6aa7815387e666939d086d0f4da01d939d9df7b52b5d1a2bf36由该root记录实际消费，status为root-consumed-limited-proved。

它的§1允许F={q≤X}全部素数，且§4(Loc)对所有充分大real X和每先fixed b成立：L=log X、A=sqrtX/L、delta=L^(-2/5)，

    sup_(delta≤|t|≤L^b) k_≤X(t,t)≤exp(−c A delta²)。

后面的(Loc<)才专门处理X=p时omit-p；不能把前一个full版本限制为prime-only。这里是完整Gram逆的actual kernel，非bare Q/Euler权。C070取X=e^j,b=2可直接使用已付界

    sup_(j^-2/5≤|t|≤j²) k_ej(t,t)
       ≤exp(−c e^(j/2)/j^(9/5))。

独立稿的Hermite diagonal K_N≤2sqrt(2N)及第四矩tail≤4N(N+1)²/T⁴，原输入三分给

    b_j=sup_(||f||∞≤1)||Pi_ej M_f E_(j²)||HS
       ≤sqrt(4sqrt2 j^(3/5))
          +(j/sqrtpi)exp(−c e^(j/2)/(2j^(9/5)))+4/j。

因此原库存已经蕴含保守的b_j²=O(j^(3/5))，C_j(r)≤O(j^(3/5))||r||1²；每fixed source窗的全complex原du单位球有同阶upper。这个旧推论已经强于两个稿件实际证明的o(j)，本次不能以弱bound变化计新数学／whole净后果。

更一般，未代入LOC以前，同一已写出的分块已经给对所有0<eta<j²的exact envelope

    b_j≤sqrt(4sqrt2 eta j)
          +[∫_(eta<|t|≤j²)k_ej(t,t)dmu(t)]^(1/2)+4/j。

它保留更细旧估计可以输入的位置，不宣称3/5最优，也不在此优化delta指数或另开参数。上述展示仅恢复已root接受的2/5版本，足以扣除本次弱upper的计功；没有新的prime estimate。

若只匹配anchor q0，O(j^(3/5))仅迫liminf c_j j^(3/5)>0，不迫该乘积趋无穷，更不迫c_j本身发散。稿件从o(j)得到的c_j j→∞仍正确，但较弱。所有允许的任意无界common calibration和actual三比值依旧OPEN。

9800/12230稿中“fixed-eta接口不能直接换moving eta”的话只限它们实际引用的那条接口。不得扩大为项目所有旧资产都没有支付moving-window；C059 LOC已支付上述量词。原证明的固定eta逻辑仍正确，不冻结其数学upper，只冻结从该简写恢复的全局缺失判断和新增净值。

## 2. 严格positive sandwich，不能升级裸trace

12230稿§3的“trace of P_j 1_S1”简写只按实际显示式消费：

    ||P_j 1_S1||HS²=Tr(1_S1 P_j 1_S1)
                   =∫_S1 k_j(t,t)dmu(t)。

不消费裸P_j1_S1∈S1或其ordinary trace。有限区间actual continuous RKHS diagonal与positive sandwich支付此HS域；不把Pi本身变trace class。这个限定不改变有效upper，9800稿已明确使用positive sandwich。

## 3. 条件、实际通道和主门分别消费

Conditional liminf delta≥(q1/q0)/5只在实际relative-remainder前件成立且分母最终正时成立，该前件尚未证明。Root的Hilbert反三角式、phase-blind logical control和Taylor refinement也不证明它；phase控制的P^(b)不是实际完整B/P/G Sonin投影，不能作C070反例。

第三稿的实际physical支持恒等式、有限Mobius/Hermite/G^-1列、Hankel下界通道及Poincare/平移／even remainder通道均需保其准确角色：B_j(g)只是一个实际非负下界量，不是正数coercivity lower，亦不已知占C_j(g)固定比例。不能由B_j(g)≤C_j(g)及B_j(g′)≥2B_j(g)/b²把同样不等式移到两个full anchors。

这些标准分块／support代数和由强旧LOC直接推出的receiver upper没有支付actual非零anchor、共同校准后的相干角度或任一实际比值。主C070测试当前既未通过，也未被反测；零分母是否无限发生亦未知。不得把本次工作降称“没有做证明”，也不得把它升成新严格方法类边界。

所有目标仍为ALL-complex physical源、原du/zero-extension Dlog、完整Γ/contact/pp/双pole；g′odd未删。只处理原固定X=e^j,N=j²，不消费其它path、receiver、source-dependent或negative/signed修补。新经典净后果、实际核心瓶颈移除和长期Goal完成均不存在于这些partial结论中。
