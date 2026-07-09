# Encode and Decode Strings

**Difficulty:** Medium

## Problem Statement

Design an algorithm to **encode** a list of strings into a single string. The encoded string is then sent over the network and **decoded** back into the original list of strings.

Machine 1 (Sender) has the following function:

```java
String encode(List<String> strs) {
    // Your implementation
    return encodedString;
}
```

Machine 2 (Receiver) has the following function:

```java
List<String> decode(String encodedString) {
    // Your implementation
    return decodedStrings;
}
```

### Workflow

Machine 1 performs:

```java
String encodedString = encode(strs);
```

The encoded string is transmitted over the network.

Machine 2 receives the encoded string and performs:

```java
List<String> decodedStrings = decode(encodedString);
```

The decoded list **must be identical** to the original input list.

In other words:

```text
decode(encode(strs)) == strs
```

Implement the `encode()` and `decode()` methods.

---

## Examples

### Example 1

**Input**

```text
strs = ["Hello", "World"]
```

**Output**

```text
["Hello", "World"]
```

**Explanation**

```java
Solution solution = new Solution();

String encodedString = solution.encode(strs);

// Machine 1 -------- encodedString --------> Machine 2

List<String> decodedStrings = solution.decode(encodedString);
```

---

### Example 2

**Input**

```text
strs = [""]
```

**Output**

```text
[""]
```

---

## Constraints

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- Each string may contain **any of the 256 valid ASCII characters**.

---

## Approach

Instead of separating strings using a delimiter (which may already exist inside the strings), encode each string using the following format:

```text
<length>#<string>
```

For example:

```text
["neet", "code", "love"]

↓

4#neet4#code4#love
```

During decoding:

1. Read the digits until the `#` character.
2. Convert those digits into an integer (length of the next string).
3. Read exactly `length` characters after `#`.
4. Repeat until the end of the encoded string.

This approach correctly handles:

- Empty strings
- Strings containing `#`
- Strings containing numbers
- Strings containing special characters
- Multi-digit string lengths

---

## Complexity Analysis

### Encoding

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

### Decoding

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(N)`

> **N** = Total number of characters across all strings.
