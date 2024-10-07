def convertToIpv6(ipv4address: str) -> str:
    # Split the IPv4 address into octets
    octets = ipv4address.split('.')
    
    # Ensure there are exactly 4 octets
    if len(octets) != 4:
        raise ValueError("Invalid IPv4 address format. Must contain exactly 4 octets.")
    
    # Convert each octet to an integer
    try:
        first_octet = int(octets[0])
        # Ensure each octet is between 0 and 255
        if not all(0 <= int(octet) <= 255 for octet in octets):
            raise ValueError("Each octet must be between 0 and 255.")
    except ValueError:
        raise ValueError("Invalid IPv4 address format. Octets must be integers.")
    
    # Check if it's a loopback address (first octet is 127)
    if first_octet == 127:
        return "::1"
    else:
        hex_octets = [format(int(octet), '02X') for octet in octets]
        ipv6_part1 = hex_octets[0] + hex_octets[1]
        ipv6_part2 = hex_octets[2] + hex_octets[3]
        ipv6_address = f"::FFFF:{ipv6_part1}:{ipv6_part2}"
        return ipv6_address
ipv4address = input("Enter an IPv4 address: ")
print(convertToIpv6(ipv4address))
