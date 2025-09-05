import { Image, View } from "react-native";

export function Logo({ style }: { style: any }) {
    return <View>
        <Image source={require("assets/logo.png")} style={style} />
    </View>
}