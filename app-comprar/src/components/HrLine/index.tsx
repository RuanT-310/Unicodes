import { StyleSheet, View } from "react-native";

export function HrLine({ marginTop }: { marginTop: number } = { marginTop: 0 }) {
    return <View style={{
        borderBottomColor: '#130505ff', // Or any color you prefer
        borderBottomWidth: StyleSheet.hairlineWidth, // Creates a very thin line
        marginTop: marginTop
      }}>

    </View>
}