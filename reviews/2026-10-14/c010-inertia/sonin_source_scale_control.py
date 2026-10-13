"""Own rational one-mode normalization control; wrong object is explicit."""
from pathlib import Path
from fractions import Fraction as F
import json
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[2]
P=BASE/'tmp/c009-liu/fresh-b-20261014/certificates'
a=json.loads((P/'source-matrices.json').read_text())
t=json.loads((P/'tail-columns.json').read_text())
def first(name):
    i,j,lo,hi=a['matrices'][name][0]
    assert i==j==0
    return F(int(lo)+int(hi),2**257)
col={row['column']:F(int(row['lo'])+int(row['hi']),2**641)
     for row in t['entries'] if row['index']==0}
L=F(17,16); norm=2*L
u=F(648,17)*(col[0]**2+col[1]**2)
correct=(first('A')+first('J0')+u)/norm
wrong=(first('A')+L**2*first('J0')+u)/norm
epsA=F(1,2**220); epsH=F(1,2**204)+F(1,2**220); sigma=F(9,2**512)
assert correct-(epsA+epsH+sigma)>F(1,32)
assert wrong+(epsA+L**2*epsH+sigma)<-F(1,8)
out={'kind':'exact-rational-normalization-negative-control',
     'source':'normalized constant Legendre mode, same half-window17/16',
     'correct_object':'A+J0+U','correct_lower_bound':'1/32',
     'wrong_object':'A+L^2*J0+U','wrong_upper_bound':'-1/8',
     'extra_L_squared_is_invalid_for_original_raw_J0':True,
     'actual_negative_R_found':False,'paid_source_error':True}
(HERE/'sonin-source-scale-control.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
