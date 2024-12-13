import pysparql_anything as sa

engine = sa.SparqlAnything()

engine.run(query='../queries/prize.sparql', output='../output/prize.ttl', format='TTL')
