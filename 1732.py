class Solution:
    def largestAltitude(self, gain):
        altitude = 0
        altitudes = [0]

        for g in gain:
            altitude += g
            altitudes.append(altitude)

        return max(altitudes)