def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def format_ip_address(binary_str):
    # Split the binary string into 4 octets of 8 bits each and convert them to decimal
    octets = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return '.'.join(str(binary_to_decimal(octet)) for octet in octets)

def parseIPHeader():
    # Taking input from the user without descriptive prompts
    header_line = input().strip()
    flag1 = input().strip()  # Although the flags are given, they are not used in parsing
    source_ip_line = input().strip()
    flag2 = input().strip()
    destination_ip_line = input().strip()
    flag3 = input().strip()
    
    # Extract the relevant fields from the header
    version = binary_to_decimal(header_line[0:4])           # Bits 0-3: Version
    protocol_number = binary_to_decimal(header_line[4:12])  # Bits 4-12: Protocol
    ttl = binary_to_decimal(header_line[12:20])             # Bits 13-20: Time to Live
    packet_length = binary_to_decimal(header_line[20:32])   # Bits 21-31: Packet Length
    
    # Determine the protocol name
    protocol_name = "TCP" if protocol_number == 6 else "UDP" if protocol_number == 17 else "Unknown"
    
    # Format source and destination IP addresses
    source_ip = format_ip_address(source_ip_line)
    destination_ip = format_ip_address(destination_ip_line)
    
    # Output the required information
    print(f"{version},{protocol_name},{ttl},{packet_length}")
    print(source_ip)
    print(destination_ip)

# Call the function to parse the IP header
parseIPHeader()
