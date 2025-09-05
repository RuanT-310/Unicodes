import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
    container: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
        margin: 10,
    },
    tabs: {
        display: "flex",
        flexDirection: "row",
        gap: 20
    },

    tabText: {
        color: "#828282",
        fontWeight: "semibold",
    },
    tabTextActive: {
        color: "black",
    },
    tabButton: {
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        gap: 5
    },
})