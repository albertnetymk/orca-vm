-module(higher_order_discrepancy).

-export([test/1]).

test(X) ->
    F =
	case X of
	    1 -> fun f/1;
	    2 -> fun g/1
	end,
    F(foo).

f(foo) -> ok.
g(bar) -> ok.
