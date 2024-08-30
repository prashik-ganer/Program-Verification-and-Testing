:x = :c1 + 10
if(:x >= 40)[
    :y = :x + :c2
]
else[
    if(:x <20 )[
    	:y = :x + :c1
    ]
    else[
    	:y = :c1
    ]
]