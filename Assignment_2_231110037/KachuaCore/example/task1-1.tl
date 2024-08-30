if :x <= 50 [
   :y = :y - :c1 -:c2
]
else [
   :y = :y - :c1
   if :x<=30[
    :y=:y+:c1
   ]
   else[
    :y=:y+:c2
   ]
]