import * as React from 'react';
import { BottomNavigation, Provider as PaperProvider, DefaultTheme } from 'react-native-paper';
import { Text } from 'react-native';
import Explore from './explore';
import Chat from './chat';
import Profile from './profile';
import Search from './search';

const ExploreView = () => <Explore></Explore>;
const SearchView = () => <Search></Search>;
const ProfileView = () => <Profile></Profile>;
const ChatView = () => <Chat></Chat>;

const theme = {
  ...DefaultTheme,
  roundness: 2,
  colors: {
    ...DefaultTheme.colors,
    primary: '#86734e',
    accent: '#f1c40f',
  },
};

const MyComponent = () => {
  const [index, setIndex] = React.useState(0);
  const [routes] = React.useState([
    { key: 'explore', title: 'Explore', icon: 'album' },
    { key: 'search', title: 'Search', icon: 'album' },
    { key: 'chat', title: 'Chat', icon: 'album' },
    { key: 'profile', title: 'Profile', icon: 'album' },
  ]);
  const renderScene = BottomNavigation.SceneMap({
    explore: ExploreView,
    search: SearchView,
    chat: ChatView,
    profile: ProfileView,
  });

  return (
    <PaperProvider theme={theme}>
      <BottomNavigation
        navigationState={{ index, routes }}
        onIndexChange={setIndex}
        renderScene={renderScene}
      />
    </PaperProvider>
  );
};

export default MyComponent;