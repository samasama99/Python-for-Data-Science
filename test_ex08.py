from time import sleep
from ex08.Loading import ft_tqdm

def test_ex08():
    print("--- Testing ft_tqdm (Visual Check) ---")
    
    # Subject Test 1
    print("Test 1: range(333)")
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    # Subject Test 2 (Same list)
    print("Test 2: tqdm(range(333))")
    # Note: We don't have the real tqdm installed, so we skip comparing 
    # perfectly, but the user can visually check.
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    
    # Edge Case: range(10, 0, -1)
    print("Test 3: Negative Range range(100, 0, -1)")
    for elem in ft_tqdm(range(100, 0, -1)):
        sleep(0.01)
    print()

if __name__ == "__main__":
    test_ex08()
