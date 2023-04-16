# python3

def read_input():
    choice = input()
    if choice == 'I':
        pat = input()
        text = input()
    elif choice == 'F':
        with open('tests/06', 'r') as f:
            pat = f.readline().strip()
            text = f.readline().strip()
    return pat, text

def get_occurrences(pat, text):
    d = 256
    q = 101
    m = len(pat)
    n = len(text)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    result = []
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if pat[j] != text[i + j]:
                    match = False
                    break
            if match:
                result.append(i)
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return result

def print_occurrences(output):
    print(' '.join(map(str, output)))

def main():
    pat, text = read_input()
    output = get_occurrences(pat, text)
    print_occurrences(output)

if __name__ == '__main__':
    main()

