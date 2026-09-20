# 400–401之后的有限任务：内在FF曲线的对角与untilt剩余域

2026-09-20。**[O] 新来源比较任务；尚未证明该候选平方满足所需几何。**
[400](../../notes/400-f1-cartier-tower-limit-and-stalk-defect.md)排除通常逆极限恢复非平凡Cartier图；
[401](../../notes/401-f1-dual-cartier-ideal-and-reflexive-collapse.md)保留实际下降的非闭理想层，
但它不局部有限生成，仍非通常Cartier数据。
本次转向内在Fargues–Fontaine曲线，先检验实际对角，避免继续只改变同一完成／对偶接口。

## 固定来源与要回答的有限问题

取379实际构造的perfectoid域C，令F=C^♭，E=Q_p。
先从已归档FF原著与Lurie讲义核对X_(F,E)的准确scheme定义，
以及untilt C是否给一个剩余域恰为C的真实点x。
“存在C值点”不等于“其剩余域等于C”，不得跳过这一比较。

候选平方暂固定为普通scheme纤维积X_(F,E)×_(Spec E)X_(F,E)。
它不同于398的C上perfectoid平方；不称其为已证明的算术绝对平方，
也不因X是一维正则scheme就假设其普通E平方是光滑曲面。

首个目标是判定这个平方中对角线在(x,x)附近是否能为有效Cartier闭子空间。
这是采用新来源前的有限准入测试，而非完整τ的存在性定理。

## 直接检验链与可能的严格障碍

1. 回到源定理核对F、C、E的前提，包括非代数闭情形、θ的满射、
   primitive元素给出的理想，以及scheme点的实际剩余域；新增来源及时保存。
2. 在x的仿射邻域直接计算对角余法模I/I²与Ω_(X/E)的关系，
   再核对Ω_(X/E)⊗κ(x)→Ω_(κ(x)/E)的满射。
   这里使用普通代数Kähler微分，不用连续微分代替。
3. 检验以下条件障碍：若对角有效Cartier且κ(x)=C，则
   dim_C Ω_(C/Q_p)≤1。
   379的C含全部t^r；尝试用1、sqrt(2)、sqrt(3)的Q线性无关及赋值
   证明t^sqrt(2)、t^sqrt(3)在Q_p上代数独立，
   从而在特征零下得到两个独立代数微分，产生矛盾。
   这条链必须独立复核，不能仅引用“FF曲线正则”或“完备域没有微分”。
4. 若障碍成立，准确停止该普通E纤维积的Cartier对角接法，
   并区分仍可能的相对untilt、其他基底或非Cartier交叉理论。
   若首项来源比较失败，保存精确原因，不把条件结论说成实际FF结论。
5. 只有实际对角准入后，才继续2、3、6对应、交叉及固定ζ比较。
   不把任意整数幂当作F的加法域自同态，也不从一个untilt点自动得到全体算术对应。

新机制是保留内在Witt／untilt几何，改变了载体和基底；
不是把400的pro塔换名。证明／停止结论需给准确范围，
仍不单独触发GOAL第十节B/C。一次只推进这一个主要来源／对角问题。


2026-09-20结算：[402](../../notes/402-f1-intrinsic-ff-diagonal-conormal-obstruction.md)及[独立复核](f1-intrinsic-ff-diagonal-independent-review.md)已完成；指定普通平方的对角理想非有限生成。下一任务见[非局部混合配对](f1-nonlocal-mixed-pairing-next-proof-plan.md)。
