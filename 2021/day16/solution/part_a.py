from aocd.models import Puzzle
from aocd import submit

length_type_id = dict([(0, 15), (1, 11)])


def get_root_packets(packets, count):
    if len(packets) == count:
        return packets
    packets.sort(key=len)
    return packets[-count:]


def get_version_number(packet):
    return int(packet[0:3], 2)


def discover_subpackets(packet, packet_sum):
    subpackets = []

    next_packet_head = 0
    last_packet_head = 0
    packet_count = 0
    while packet_count < 0 or packet_count != packet_sum:
        if int(packet[last_packet_head + 3:last_packet_head + 6], 2) == 4:
            for i in range(last_packet_head + 6, len(packet), 5):
                if int(packet[i]) == 0:
                    next_packet_head = i + 5
                    break
        else:
            if int(packet[last_packet_head + 6]) == 0:
                next_packet_head += 22 + int(packet[last_packet_head + 7:last_packet_head + 22], 2)
                print(next_packet_head)
                subpackets.extend(discover_subpackets(packet[last_packet_head + 22:next_packet_head], -1))
            else:
                next_packet_head += 18
                subpacket_count = int(packet[last_packet_head + 7:last_packet_head + 18], 2)
                container = discover_subpackets(packet[last_packet_head + 18:len(packet)], subpacket_count)
                subpackets.extend(container)
                root_packets = get_root_packets(container[:], subpacket_count)

                next_packet_head += sum(len(p) for p in root_packets)

        subpackets.append(packet[last_packet_head:next_packet_head])
        last_packet_head = next_packet_head
        if next_packet_head == len(packet) or int(packet[next_packet_head:len(packet)]) == 0:
            break
        packet_count += 1
    return subpackets


def return_solution(packet):
    subpackets = discover_subpackets(packet, -1)
    versions = list(map(get_version_number, subpackets))
    return sum(versions)


def split_input(puzzle):
    binary = ""

    for char in puzzle:
        binary += bin(int(char, 16))[2:].zfill(4)

    return binary


def main():
    puzzle = Puzzle(year=2021, day=16)
    # return_solution(split_input(puzzle.input_data))
    submit(return_solution(split_input(puzzle.input_data)), part="a", day=16, year=2021)


if __name__ == '__main__':
    main()
