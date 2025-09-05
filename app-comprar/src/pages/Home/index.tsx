import { StatusBar } from 'expo-status-bar';
import { Keyboard, View } from 'react-native';
import { styles } from "./styles"
import { Button } from '@/components/Button';
import { Logo } from '@/components/Logo';
import { Input } from '@/components/Input';
import { useState } from 'react';
import { Tabs } from '@/components/Tabs';
import { ItemList } from '@/components/ItemList';
import { ShoppingItem } from '@/interfaces/shopping-item';

export function Home() {
  const [text, setText] = useState('');
  const [items, setItems] = useState<ShoppingItem[]>([]);
  const [filter, setFilter] = useState<'pending' | 'completed'>('pending');

  const handleAddItem = (text: string) => {
    const newItem: ShoppingItem = {
      id: new Date().getTime().toString(), // Melhor forma de gerar um ID único
      text,
      isCompleted: false,
    };
    setItems((prevItems) => [newItem, ...prevItems]);
    setText('');
    Keyboard.dismiss();
  };

  const handleToggleItem = (id: string) => {
    setItems((prevItems) =>
      prevItems.map((item) =>
        item.id === id ? { ...item, isCompleted: !item.isCompleted } : item
      )
    );
  };

  const handleDeleteItem = (id: string) => {
    setItems((prevItems) => prevItems.filter((item) => item.id !== id));
  };
  
  const handleClearCompleted = () => {
    setItems((prevItems) => prevItems.filter((item) => filter === 'pending' ? item.isCompleted : !item.isCompleted));
  };

  const filteredItems = items.filter((item) =>
    filter === 'pending' ? !item.isCompleted : item.isCompleted
  );
  return (
    <View style={styles.container}>
        <Logo style={styles.logo}/>
        <Input 
        placeholder='O que você precisa comprar?'
        value={text}
        onChangeText={setText}
        />
        <Button title='Adicionar' onPress={() => handleAddItem(text)}/>
      <StatusBar style="auto" />
      <View style={styles.listContainer}>
        <Tabs
          filter={filter}
          onSelectFilter={setFilter}
          onClear={handleClearCompleted}
        />
        <View style={styles.hrLine} />
        <ItemList
          filteredItems={filteredItems}
          handleToggleItem={handleToggleItem}
          handleDeleteItem={handleDeleteItem}
        />
      </View>
    </View>
  );
}