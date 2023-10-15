import python

from Expr evalExpr
where
  evalExpr instanceof EvalExpr
select evalExpr, "Use of eval function in Python"
