
# coding: utf-8

# In[ ]:

from concurrent.futures import ProcessPoolExecutor
from src import simulate, prepare_first_conditions


if __name__ == "__main__":

    args = prepare_first_conditions()

    results = []
    with ProcessPoolExecutor(max_workers=4) as executor:
        for arg in args:
            results.append(executor.submit(simulate, *arg))
    print(results)


# %%
