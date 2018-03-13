def get_traffic_classes(output_data):
    traffic_classes = re.search(r'(\"class-var\".+)', output_data, re.MULTILINE | re.IGNORECASE)
    traffic_classes = (traffic_classes.group())
    traffic_classes = traffic_classes.split('","')
    traffic_classes.pop(0)
    return traffic_classes


def get_traffic_volumes(output_data):
    traffic_volumes = re.search(r'(\"bytes\".+)', output_data, re.MULTILINE | re.IGNORECASE)
    traffic_volumes = (traffic_volumes.group())
    traffic_volumes = traffic_volumes.split(',')
    traffic_volumes.pop(0)
    return traffic_volumes


def get_average_utilization(output_data):

    average_utilization = re.search(r'(\"avg-bps\".+)', output_data, re.MULTILINE | re.IGNORECASE)
    average_utilization = (average_utilization.group())
    average_utilization = average_utilization.split(',')
    average_utilization.pop(0)
    return average_utilization


# elastic search :)
# direction => "in" | "out" | all
# order_ by => "name" | "volume" | "utilization"
# order => "asc" | "desc"
# size => number of top entries
def get_traffic_classes_data(a, b, c, direction, order_by, order, size):
    traffic_classes = a
    traffic_volumes = b
    average_utilization = c
    traffic_classes_data = {}
    traffic_classes_data_tmp = {}
    traffic_classes_data_all = []
    traffic_classes_data_inbound = []
    traffic_classes_data_outbound = []

    for index, value in enumerate(traffic_volumes):
        traffic_classes_data_tmp[traffic_classes[index]] = {}
        traffic_classes_data_tmp[traffic_classes[index]] = (traffic_classes[index], int(traffic_volumes[index]),
                                                        int(average_utilization[index]))
    for key, value in traffic_classes_data_tmp.iteritems():
        tmp = value  # or tmp = (key, value)
        traffic_classes_data_all.append(tmp)
        if re.search(r'(/Inbound.*)', str(tmp), re.IGNORECASE) is not None:
            traffic_classes_data_inbound.append(tmp)
        elif re.search(r'(/Outbound.*)', str(tmp), re.IGNORECASE) is not None:
            traffic_classes_data_outbound.append(tmp)

    if direction == "in":
        traffic_classes_data = traffic_classes_data_inbound
    elif direction == "out":
        traffic_classes_data = traffic_classes_data_outbound
    elif direction == "all":
        traffic_classes_data = traffic_classes_data_all

    if order_by == "name":
        order_by_index = int(0)
    elif order_by == "volume":
        order_by_index = int(1)
    elif order_by == "utilization":
        order_by_index = int(2)

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
    get_traffic_classes_data(get_traffic_classes(output), get_traffic_volumes(output), get_average_utilization(output),
                             "all", "volume", "desc", 20)


if __name__ == "__main__":
    main()
