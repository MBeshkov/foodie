import React from 'react';
import {
  SafeAreaView,
  View,
  FlatList,
  StyleSheet,
  Text,
  StatusBar,
  TouchableOpacity,
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { BottomNavigation } from 'react-native-paper';

const DATA = [
  {
    id: 'bd7acbea-c1b1-46c2-aed5-3ad53abb28ba',
    title: 'Food A',
    by: 'A',
  },
  {
    id: '3ac68afc-c605-48d3-a4f8-fbd91aa97f63',
    title: 'Food B',
    by: 'B',
  },
  {
    id: '58694a0f-3da1-471f-bd96-145571e29d72',
    title: 'Food C',
    by: 'C',
  },
];

const Item = ({ title,by }) => (
  <View style={styles.item}>
    <Text style={styles.title}>{title}</Text>
    <Text style={styles.desc}>{by}</Text>
  </View>
);

const List = ({ navigation }) => {
  const renderItem = ({ item }) => (
    <TouchableOpacity 
    onPress={() => navigation.navigate("Details", {title: item.title, by: item.by})}
    >
      <Item title={item.title} by={item.by}/>
    </TouchableOpacity>
  );
  return(
    <FlatList
      data={DATA}
      renderItem={renderItem}
      keyExtractor={item => item.id}
      onPress = {() => navigation.navigate("Details")}
    />
  )
};

const Details = ({ route, navigation }) => {
  const {title, by} = route.params;
  return(
    <Text>
      {JSON.stringify(title)}
      {JSON.stringify(by)}
    </Text>
  );
};

const Stack = createNativeStackNavigator();

const Explore = () => {

  return (
    <SafeAreaView style={styles.container}>
      <NavigationContainer>
        <Stack.Navigator screenOptions={{ headerShown: false }}>
          <Stack.Screen
            name="List"
            component={List}
          />
          <Stack.Screen
            name="Details"
            component={Details}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: StatusBar.currentHeight || 0,
  },
  item: {
    backgroundColor: '#c2aa7b',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 27,
  },
  desc: {
    fontSize: 18,
  },
});

export default Explore;