all:
	cabal run --ghc-options="-L/usr/lib/ghc-9.2.8/site-local/regex-tdfa-1.3.2.2 -dynamic"

format:
	ormolu -i **/*.hs
