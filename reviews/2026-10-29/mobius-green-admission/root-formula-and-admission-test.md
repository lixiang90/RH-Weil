# 实际 Möbius Green 响应：只准一个强旧／定义域比较

2026-10-29；G20261027/runtime1793085111，原0c4f基线。恢复已现场核 main=551b05428409b103d3573028823de8a3cb414f40、tree=add13a59768a68452db5d8eeefc414a956894d88、parent=615e91f59ae90cf940d5060b0406d45d7569c2f7，与独立GitHub ref/commit/tree匹配且初始工作树clean。上次条件已满足，不重推。

本门不是C056/593，不延长已停Koszul/graph预算。518已明确给实际Möbius逆；要核的是一个具体的临界Green范数test及其最强旧净值，不是再泛查来源。

## 冻结实物、角色及可判门

复物理源 r(u)=e^(u/2)f(u)，f∈S_exp,C。取

    V_r(t)=Σ_(n≥1) μ(n)n^(-1/2) r(log n−t)
          =2e^(-t/2) θ_f(e^(-t)),
    θ_f(x)=(1/2)Σ_(n≥1) μ(n)f(log(nx)).

后式就是518(11)，不是新的源公式。405真实Eη(u)=2Ση(ne^u)，故候选精确消去证书应为

    V_(e^(u/2)Eη)(t)=2e^(-t/2)η(e^(-t)).

保留原因子2，bare f与physical r不合并。这里只拟把L²(dt)响应当解析可忽略类；它尚不是局部单位、主除子或几何Green cocycle。它会消全部I而不只是双次数零P_an，必须检查两个degree方向损失。537全Γ/contact/proper powers/双pole目标不被此响应改写。

**准入问题三句：** 独立算术系数是实际μ，但其逆公式已属518旧资产。最便宜不同test是：任何非零compact smooth r是否均使V_r不在critical L²(dt)，而所有真实Eη响应在L²，且此差别是否仅是旧zero-jet商的改写。只有扣405/518–520和080–082最强后，实际给新principal／同对象primitive输入或改变选择的净后果，才考虑数学合同；若为标准直接组合则old0止，不续damping/权/源族/章节。

## 初始证明路线及审查责任（尚非根消费）

compact supp r⊂[-L,L]时响应局部有限，t<−L为0；拟有

    ∫ V_r(t)e^(-zt)dt=M_r(z)/ζ(1/2+z), Re z>1/2,
    M_r(z)=∫r(u)e^(zu)du.

若V_r∈L²，则左边延到Re z>0且受e^(σL)||V_r||₂/(2σ)^(1/2)控制。非零compact源的M_r有限指数型，零点count O_r(T)；ζ经RvM和FE有至少约一半TlogT的右半／边界零点，按重数计。拟存在未消pole：interior违反解析，boundary整阶pole违反σ^(-1/2)界。审查须核换序、半面延拓、重数、Jensen和边界比较，不假RH或简单性。

两个独占输出：domain-and-critical-energy-test.md负责实际域／范数／证明；strongest-old-and-principal-scope.md负责最强旧与几何角色。Root消费前它们都只是draft。若需要独立fresh，只审此已形成公式及根前件，不借题扩张。当前cadence2/history56/latest592/formal18与manifest131保持，无外部新query/primary/PDF/下载/数值。

即使证明成立，也不等于有正Hilbert商：L²在L²_loc的局部拓扑下稠密，裸商可能非Hausdorff；不把非零代数类升级为可用正度量。不同Green、secondary、强域或有费修复不由此排除。完整Goal仍active/open/noteligible。
