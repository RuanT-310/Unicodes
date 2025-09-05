import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import Icon from 'react-native-vector-icons/Feather';
import { styles } from './styles';

//import { ShoppingItem } from '../../types';
export interface ShoppingItem {
  id: string;
  text: string;
  isCompleted: boolean;
}
interface Props {
  item: ShoppingItem;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export const ListItem: React.FC<Props> = ({ item, onToggle, onDelete }) => {
  return (
    <View style={styles.container}>
      <TouchableOpacity onPress={() => onToggle(item.id)} style={styles.checkbox}>
        {item.isCompleted ? (
          <Icon name="check-circle" size={20} color="#6A0DAD" />
        ) : (
          <Icon name="circle" size={20} color="#6A0DAD" />
        )}
      </TouchableOpacity>
      <Text style={[styles.text, item.isCompleted && styles.textCompleted]}>
        {item.text}
      </Text>
      <TouchableOpacity onPress={() => onDelete(item.id)} style={styles.deleteButton}>
        <Icon name="trash-2" size={20} color="#DC143C" />
      </TouchableOpacity>
    </View>
  );
};