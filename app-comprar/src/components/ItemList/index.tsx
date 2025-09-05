import { FlatList, Text, View } from "react-native"
import { ListItem } from "../ListItem"
import { styles } from "./styles";
import { ShoppingItem } from "@/interfaces/shopping-item";

interface Props {
    filteredItems: ShoppingItem[];
    handleToggleItem: (id: string) => void;
    handleDeleteItem: (id: string) => void;
}
export function ItemList({ filteredItems, handleToggleItem, handleDeleteItem }: Props) {
    if (filteredItems.length === 0)
        return <View style={styles.emptyContainer}>
            <Text style={styles.emptyText}>
                Nenhum item Aqui
            </Text>
        </View>
    return <FlatList
        data={filteredItems}
        renderItem={({ item }) => (
            <ListItem
            item={item}
            onToggle={handleToggleItem}
            onDelete={handleDeleteItem}
            />
        )}
        keyExtractor={(item) => item.id}
        />
}