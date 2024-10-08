def defang_ip_addr(address):
    """
    :type address: str
    :rtype: str
    """
    address = address.replace(".", "[.]")
    return address


if __name__ == '__main__':
    address1 = "1.1.1.1"
    print(defang_ip_addr(address1))

    address2 = "255.100.50.0"
    print(defang_ip_addr(address2))