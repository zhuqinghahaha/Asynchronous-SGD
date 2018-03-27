import argparse


def configuration():
    parser = argparse.ArgumentParser(description='PyTorch WideResNet Training')
    parser.add_argument('--dataset', default='cifar10', type=str,
                        help='dataset (cifar10 [default] or cifar100)')
    parser.add_argument('--epochs', default=200, type=int,
                        help='number of total epochs to run')
    parser.add_argument('--start-epoch', default=0, type=int,
                        help='manual epoch number (useful on restarts)')
    parser.add_argument('-b', '--batch-size', default=128, type=int,
                        help='mini-batch size (default: 128)')
    parser.add_argument('--lr', '--learning-rate', default=0.1, type=float,
                        help='initial learning rate')
    parser.add_argument('--momentum', default=0.9, type=float, help='momentum')
    parser.add_argument('--nesterov', default=True, type=bool, help='nesterov momentum')
    parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                        help='weight decay (default: 5e-4)')
    parser.add_argument('--layers', default=28, type=int,
                        help='total number of layers (default: 28)')
    parser.add_argument('--widen-factor', default=10, type=int,
                        help='widen factor (default: 10)')
    parser.add_argument('--droprate', default=0, type=float,
                        help='dropout probability (default: 0.0)')
    parser.add_argument('--no-augment', dest='augment', action='store_false',
                        help='whether to use standard augmentation (default: True)')
    parser.add_argument('--resume', default='', type=str,
                        help='path to latest checkpoint (default: none)')
    parser.add_argument('--name', default='WideResNet-28-10', type=str,
                        help='name of experiment')
    parser.add_argument('--sim_num', default='1', type=int,
                        help='simulation id')
    parser.add_argument('--workers_num', default=1, type=int,
                        help='number of workers')
    parser.add_argument('--grad_clip', default=2, type=float,
                        help='gradient clipping threshold')
    parser.add_argument('--id', default=2000, type=int,
                        help='simulation number')
    # parser.add_argument('--gpu_num', default=3, type=int,
    #                     help='gpu number')
    parser.add_argument('--optimizer', default='asynchronous', type=str,
                        help='type of optimizer (synchronous/asynchronous/elastic)')
    parser.set_defaults(augment=True)
    args = parser.parse_args()
    args.iterations_per_epoch = 50000 // args.batch_size
    return args
