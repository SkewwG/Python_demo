import gevent

def print_alpha(alpha):
    return alpha

def print_digit():
    pass

if __name__ == '__main__':
    jobs1 = [gevent.spawn(print_alpha,chr(alpha)) for alpha in range(97,123)]
    gevent.joinall(jobs1)
    for job1 in jobs1:
        alpha = job1.value
