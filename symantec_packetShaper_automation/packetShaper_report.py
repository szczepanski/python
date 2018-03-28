import re
import output_data
from decimal import *

output_1 = output_data.output_1
output_2 = output_data.output_2
output_3 = output_data.output_3
output_4 = output_data.output_4
output_5 = output_data.output_5
output_6 = output_data.output_6

avg_bps_tmp = []
peak_bps_tmp = []
bytes_tmp = []

# 1. get 6: traffic_classes, avg_bps, peak_bps, guar_rate_fails, bytes, pkts
def get_output_1_data(output_1):
    # traffic class
    traffic_classes = re.search(r'(\"class-var\".+)', output_1, re.MULTILINE | re.IGNORECASE)
    traffic_classes = (traffic_classes.group())
    traffic_classes = traffic_classes.split('","')
    traffic_classes.pop(0)

    # avg_bps
    avg_bps = re.search(r'(\"avg-bps\".+)', output_1, re.MULTILINE | re.IGNORECASE)
    avg_bps = (avg_bps.group())
    avg_bps = avg_bps.split(',')
    avg_bps.pop(0)
    # convert bps to Mbps
    getcontext().prec = 4
    for key in avg_bps:
        key_tmp = Decimal(key) / Decimal(1000000)
        avg_bps_tmp.append(key_tmp)
    avg_bps = avg_bps_tmp

    # peak_bps
    peak_bps = re.search(r'(\"peak-bps\".+)', output_1, re.MULTILINE | re.IGNORECASE)
    peak_bps = (peak_bps.group())
    peak_bps = peak_bps.split(',')
    peak_bps.pop(0)
    # convert bps to Mbps
    getcontext().prec = 4
    for key in peak_bps:
        key_tmp = Decimal(key) / Decimal(1000000)
        peak_bps_tmp.append(key_tmp)
        peak_bps = peak_bps_tmp

    # guar_rate_fails
    guar_rate_fails = re.search(r'(\"guar-rate-fails\".+)', output_1, re.MULTILINE | re.IGNORECASE)
    guar_rate_fails = (guar_rate_fails.group())
    guar_rate_fails = guar_rate_fails.split(',')
    guar_rate_fails.pop(0)

    # bytes
    bytes = re.search(r'(\"bytes\".+)', output_1, re.MULTILINE | re.IGNORECASE)
    bytes = (bytes.group())
    bytes = bytes.split(',')
    bytes.pop(0)
    # convert bytes to Gb (GBytes)
    getcontext().prec = 4
    for key in bytes:
        key_tmp = Decimal(key) / Decimal(1000000000)
        bytes_tmp.append(key_tmp)
        bytes = bytes_tmp

    # pkts
    pkts = re.search(r'(\"pkts\".+)', output_1, re.MULTILINE | re.IGNORECASE)
    pkts = (pkts.group())
    pkts = pkts.split(',')
    pkts.pop(0)

    return traffic_classes, avg_bps, peak_bps, guar_rate_fails, bytes, pkts


# 2. get 5: tcp_efficiency, tcp_retx-pkts, tcp_retx-bytes, tcp_conn_inits, tcp_conn_aborts
def get_output_2_data(output_2):
    # tcp_efficiency %
    tcp_efficiency = re.search(r'(\"tcp-efficiency%\".+)', output_2, re.MULTILINE | re.IGNORECASE)
    tcp_efficiency = (tcp_efficiency.group())
    tcp_efficiency = tcp_efficiency.split(',')
    tcp_efficiency.pop(0)

    # tcp_retx_pkts
    tcp_retx_pkts = re.search(r'(\"tcp-retx-pkts\".+)', output_2, re.MULTILINE | re.IGNORECASE)
    tcp_retx_pkts = (tcp_retx_pkts.group())
    tcp_retx_pkts = tcp_retx_pkts.split(',')
    tcp_retx_pkts.pop(0)

    # tcp_retx_bytes
    tcp_retx_bytes = re.search(r'(\"tcp-retx-bytes\".+)', output_2, re.MULTILINE | re.IGNORECASE)
    tcp_retx_bytes = (tcp_retx_bytes.group())
    tcp_retx_bytes = tcp_retx_bytes.split(',')
    tcp_retx_bytes.pop(0)

    # tcp_conn_inits
    tcp_conn_inits = re.search(r'(\"tcp-conn-inits\".+)', output_2, re.MULTILINE | re.IGNORECASE)
    tcp_conn_inits = (tcp_conn_inits.group())
    tcp_conn_inits = tcp_conn_inits.split(',')
    tcp_conn_inits.pop(0)

    # tcp_conn_aborts
    tcp_conn_aborts = re.search(r'(\"tcp-conn-aborts\".+)', output_2, re.MULTILINE | re.IGNORECASE)
    tcp_conn_aborts = (tcp_conn_aborts.group())
    tcp_conn_aborts = tcp_conn_aborts.split(',')
    tcp_conn_aborts.pop(0)

    return tcp_efficiency, tcp_retx_pkts, tcp_retx_bytes, tcp_conn_inits, tcp_conn_aborts


# 3. get 3: tcp_conn_server_ignores, tcp_conn_server_refuses, tcp_early_retx_toss_pkts
def get_output_3_data(output_3):
    # tcp_conn_server_ignores
    tcp_conn_server_ignores = re.search(r'(\"tcp-conn-server-ignores\".+)', output_3, re.MULTILINE | re.IGNORECASE)
    tcp_conn_server_ignores = (tcp_conn_server_ignores.group())
    tcp_conn_server_ignores = tcp_conn_server_ignores.split(',')
    tcp_conn_server_ignores.pop(0)

    # tcp_conn_server_refuses
    tcp_conn_server_refuses = re.search(r'(\"tcp-conn-server-refuses\".+)', output_3, re.MULTILINE | re.IGNORECASE)
    tcp_conn_server_refuses = (tcp_conn_server_refuses.group())
    tcp_conn_server_refuses = tcp_conn_server_refuses.split(',')
    tcp_conn_server_refuses.pop(0)

    # tcp_early_retx_toss_pkts
    tcp_early_retx_toss_pkts = re.search(r'(\"tcp-early-retx-toss-pkts%\".+)', output_3, re.MULTILINE | re.IGNORECASE)
    tcp_early_retx_toss_pkts = (tcp_early_retx_toss_pkts.group())
    tcp_early_retx_toss_pkts = tcp_early_retx_toss_pkts.split(',')
    tcp_early_retx_toss_pkts.pop(0)

    return tcp_conn_server_ignores, tcp_conn_server_refuses, tcp_early_retx_toss_pkts


# 4. get 2: total_delay_avg, network_delay_avg
def get_output_4_data(output_4):
    # total_delay_avg
    total_delay_avg = re.search(r'(\"total-delay-avg\".+)', output_4, re.MULTILINE | re.IGNORECASE)
    total_delay_avg = (total_delay_avg.group())
    total_delay_avg = total_delay_avg.split(',')
    total_delay_avg.pop(0)

    # network_delay_avg
    network_delay_avg = re.search(r'(\"network-delay-avg\".+)', output_4, re.MULTILINE | re.IGNORECASE)
    network_delay_avg = (network_delay_avg.group())
    network_delay_avg = network_delay_avg.split(',')
    network_delay_avg.pop(0)

    return total_delay_avg, network_delay_avg


# 5. get 2: server_delay_avg, total_delay_threshold
def get_output_5_data(output_5):
    # server_delay_avg
    server_delay_avg = re.search(r'(\"server-delay-avg\".+)', output_5, re.MULTILINE | re.IGNORECASE)
    server_delay_avg = (server_delay_avg.group())
    server_delay_avg = server_delay_avg.split(',')
    server_delay_avg.pop(0)

    # total_delay_threshold
    total_delay_threshold = re.search(r'(\"total-delay-threshold\".+)', output_5, re.MULTILINE | re.IGNORECASE)
    total_delay_threshold = (total_delay_threshold.group())
    total_delay_threshold = total_delay_threshold.split(',')
    total_delay_threshold.pop(0)

    return server_delay_avg, total_delay_threshold


# 6. get 2: normalized_network_delay_avg, avg_round_trip_time
def get_output_6_data(output_6):
    # normalized_network_delay_avg
    normalized_network_delay_avg = re.search(r'(\"normalized-network-delay-avg\".+)', output_6, re.MULTILINE | re.IGNORECASE)
    normalized_network_delay_avg = (normalized_network_delay_avg.group())
    normalized_network_delay_avg = normalized_network_delay_avg.split(',')
    normalized_network_delay_avg.pop(0)

    # avg_round_trip_time
    avg_round_trip_time = re.search(r'(\"avg-round-trip-time\".+)', output_6, re.MULTILINE | re.IGNORECASE)
    avg_round_trip_time = (avg_round_trip_time.group())
    avg_round_trip_time = avg_round_trip_time.split(',')
    avg_round_trip_time.pop(0)

    return normalized_network_delay_avg, avg_round_trip_time


# order_ by =>
# order => "asc" | "desc"
# size => number of top entries
def get_traffic_classes_data(traffic_class_tree, order_by, order, size):
    traffic_classes = get_output_1_data(output_1)[0]  # 0
    avg_bps = get_output_1_data(output_1)[1]  # 1
    peak_bps = get_output_1_data(output_1)[2]  # 2
    guar_rate_fails = get_output_1_data(output_1)[3]  # 3
    bytes = get_output_1_data(output_1)[4]  # 4
    pkts = get_output_1_data(output_1)[5]  # 5
    tcp_efficiency = get_output_2_data(output_2)[0]  # 6
    tcp_retx_pkts = get_output_2_data(output_2)[1]  # 7
    tcp_retx_bytes = get_output_2_data(output_2)[2]  # 8
    tcp_conn_inits = get_output_2_data(output_2)[3]  # 9
    tcp_conn_aborts = get_output_2_data(output_2)[4]  # 10
    tcp_conn_server_ignores = get_output_3_data(output_3)[0]  # 11
    tcp_conn_server_refuses = get_output_3_data(output_3)[1]  # 12
    tcp_early_retx_toss_pkts = get_output_3_data(output_3)[2]  # 13
    total_delay_avg = get_output_4_data(output_4)[0]  # 14
    network_delay_avg = get_output_4_data(output_4)[1]  # 15
    server_delay_avg = get_output_5_data(output_5)[0]  # 16
    total_delay_threshold = get_output_5_data(output_5)[1]  # 17
    normalized_network_delay_avg = get_output_6_data(output_6)[0]  # 18
    avg_round_trip_time = get_output_6_data(output_6)[1]  # 19

    traffic_classes_data = []
    traffic_classes_data_tmp = {}

    for index, value in enumerate(traffic_classes):
        traffic_classes_data_tmp[traffic_classes[index]] = {}
        traffic_classes_data_tmp[traffic_classes[index]] = (traffic_classes[index], Decimal(avg_bps[index]),
                                                            Decimal(peak_bps[index]), int(guar_rate_fails[index]),
                                                            Decimal(bytes[index]), int(pkts[index]),
                                                            int(tcp_efficiency[index]), int(tcp_retx_pkts[index]),
                                                            int(tcp_retx_bytes[index]), int(tcp_conn_inits[index]),
                                                            int(tcp_conn_aborts[index]),
                                                            int(tcp_conn_server_ignores[index]),
                                                            int(tcp_conn_server_refuses[index]),
                                                            int(tcp_early_retx_toss_pkts[index]),
                                                            int(total_delay_avg[index]), int(network_delay_avg[index]),
                                                            int(server_delay_avg[index]),
                                                            int(total_delay_threshold[index]),
                                                            int(normalized_network_delay_avg[index]),
                                                            int(avg_round_trip_time[index])
                                                            )
    traffic_class_regex = re.compile(r'(' + traffic_class_tree + ')', re.IGNORECASE)

    for key, value in traffic_classes_data_tmp.iteritems():
        tmp = value  # or tmp = (key, value)

        if traffic_class_regex.search(str(tmp)):
            traffic_classes_data.append(tmp)

    if order_by == "traffic_classes":
        order_by_index = int(0)

    elif order_by == "avg_bps":
        order_by_index = int(1)

    elif order_by == "peak_bps":
        order_by_index = int(2)

    elif order_by == "guar_rate_fails":
        order_by_index = int(3)

    elif order_by == "bytes":
        order_by_index = int(4)

    elif order_by == "pkts":
        order_by_index = int(5)

    elif order_by == "tcp_efficiency":
        order_by_index = int(6)

    elif order_by == "tcp_retx_pkts":
        order_by_index = int(7)

    elif order_by == "tcp_retx_bytes":
        order_by_index = int(8)

    elif order_by == "tcp_conn_inits":
        order_by_index = int(9)

    elif order_by == "tcp_conn_aborts":
        order_by_index = int(10)

    elif order_by == "tcp_conn_server_ignores":
        order_by_index = int(11)

    elif order_by == "tcp_conn_server_refuses":
        order_by_index = int(12)

    elif order_by == "tcp_early_retx_toss_pkts":
        order_by_index = int(13)

    elif order_by == "total_delay_avg":
        order_by_index = int(14)

    elif order_by == "network_delay_avg":
        order_by_index = int(15)

    elif order_by == "server_delay_avg":
        order_by_index = int(16)

    elif order_by == "total_delay_threshold":
        order_by_index = int(17)

    elif order_by == "normalized_network_delay_avg":
        order_by_index = int(18)

    elif order_by == "avg_round_trip_time":
        order_by_index = int(19)

    def take_index(elem):
        return elem[order_by_index]

    traffic_classes_data.sort(key=take_index)

    if order == "asc":
        pass
    elif order == "desc":
        traffic_classes_data.reverse()

    # if type(size) = int:
    print (traffic_classes_data[0:size])


def main():
    get_traffic_classes_data("/", "bytes", "desc", 100)


if __name__ == "__main__":
    main()

