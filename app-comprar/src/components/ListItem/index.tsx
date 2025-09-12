import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import {CircleDashedIcon, CircleCheckIcon, Trash2Icon} from "lucide-react-native"
import { styles } from './styles';
import { HrLine } from '../HrLine';
import { ShoppingItem } from '@/interfaces/shopping-item';
interface Props {
  item: ShoppingItem;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}
export const ListItem: React.FC<Props> = ({ item, onToggle, onDelete }) => {
  return (<>
    <View style={styles.container}>
      <View style={styles.pressContent}>
        <TouchableOpacity onPress={() => onToggle(item.id)}>
          {item.isCompleted ? (
            <CircleCheckIcon size={20} color="#2C46B1" />
          ) : (
            <CircleDashedIcon size={20} color="#1E1E1E" />
          )}
        </TouchableOpacity>
        <Text>
          {item.text}
        </Text>
      </View>
      <TouchableOpacity onPress={() => onDelete(item.id)} >
        <Trash2Icon size={20} color="#828282" />
      </TouchableOpacity>
    </View>
    <HrLine marginTop={1}/>
    </>
  );
};