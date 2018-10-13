package com.abc.xyz.main.search.users;

import com.abc.xyz.main.base.BaseFragmentView;
import com.abc.xyz.model.Profile;

import java.util.List;

public interface SearchUsersView extends BaseFragmentView {
    void onSearchResultsReady(List<Profile> profiles);

    void showLocalProgress();

    void hideLocalProgress();

    void showEmptyListLayout();

    void updateSelectedItem();
}
