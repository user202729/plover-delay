import plover  # type: ignore
import time

def delay(engine: 'plover.engine.StenoEngine', amount: str)->None:
	print(amount, float(amount))
	time.sleep(float(amount))
